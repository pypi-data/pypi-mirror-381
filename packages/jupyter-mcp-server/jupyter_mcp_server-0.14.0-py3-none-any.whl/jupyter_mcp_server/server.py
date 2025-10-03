# Copyright (c) 2023-2024 Datalayer, Inc.
#
# BSD 3-Clause License

import asyncio
import difflib
import logging
import time
from typing import Union, Optional
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

import click
import httpx
import uvicorn
from fastapi import Request
from jupyter_kernel_client import KernelClient
from jupyter_nbmodel_client import (
    NbModelClient,
    get_notebook_websocket_url,
)
from jupyter_server_api import (
    JupyterServerClient,
    NotFoundError
)
from mcp.server import FastMCP
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware

from jupyter_mcp_server.models import DocumentRuntime, CellInfo
from jupyter_mcp_server.utils import extract_output, safe_extract_outputs, format_cell_list, get_surrounding_cells_info
from jupyter_mcp_server.config import get_config, set_config
from jupyter_mcp_server.notebook_manager import NotebookManager
from typing import Literal, Union
from mcp.types import ImageContent


###############################################################################


logger = logging.getLogger(__name__)


###############################################################################

class FastMCPWithCORS(FastMCP):
    def streamable_http_app(self) -> Starlette:
        """Return StreamableHTTP server app with CORS middleware
        See: https://github.com/modelcontextprotocol/python-sdk/issues/187
        """
        # Get the original Starlette app
        app = super().streamable_http_app()
        
        # Add CORS middleware
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],  # In production, should set specific domains
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )        
        return app
    
    def sse_app(self, mount_path: str | None = None) -> Starlette:
        """Return SSE server app with CORS middleware"""
        # Get the original Starlette app
        app = super().sse_app(mount_path)
        # Add CORS middleware
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],  # In production, should set specific domains
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )        
        return app


###############################################################################


mcp = FastMCPWithCORS(name="Jupyter MCP Server", json_response=False, stateless_http=True)

# Initialize the unified notebook manager
notebook_manager = NotebookManager()


###############################################################################


def __create_kernel() -> KernelClient:
    """Create a new kernel instance using current configuration."""
    config = get_config()
    try:
        # Initialize the kernel client with the provided parameters.
        kernel = KernelClient(
            server_url=config.runtime_url, 
            token=config.runtime_token, 
            kernel_id=config.runtime_id
        )
        kernel.start()
        logger.info("Kernel created and started successfully")
        return kernel
    except Exception as e:
        logger.error(f"Failed to create kernel: {e}")
        raise

def __start_kernel():
    """Start the Jupyter kernel with error handling (for backward compatibility)."""
    try:
        # Remove existing default notebook if any
        if "default" in notebook_manager:
            notebook_manager.remove_notebook("default")
        
        # Create and set up new kernel
        kernel = __create_kernel()
        notebook_manager.add_notebook("default", kernel)
        logger.info("Default notebook kernel started successfully")
    except Exception as e:
        logger.error(f"Failed to start kernel: {e}")
        raise


def __ensure_kernel_alive() -> KernelClient:
    """Ensure kernel is running, restart if needed."""
    current_notebook = notebook_manager.get_current_notebook() or "default"
    return notebook_manager.ensure_kernel_alive(current_notebook, __create_kernel)


async def __execute_cell_with_timeout(notebook, cell_index, kernel, timeout_seconds=300):
    """Execute a cell with timeout and real-time output sync."""
    start_time = time.time()
    
    def _execute_sync():
        return notebook.execute_cell(cell_index, kernel)
    
    executor = ThreadPoolExecutor(max_workers=1)
    try:
        future = executor.submit(_execute_sync)
        
        while not future.done():
            elapsed = time.time() - start_time
            if elapsed > timeout_seconds:
                future.cancel()
                raise asyncio.TimeoutError(f"Cell execution timed out after {timeout_seconds} seconds")
            
            await asyncio.sleep(2)
            try:
                # Try to force document sync using the correct method
                ydoc = notebook._doc
                if hasattr(ydoc, 'flush') and callable(ydoc.flush):
                    ydoc.flush()  # Flush pending changes
                elif hasattr(notebook, '_websocket') and notebook._websocket:
                    # Force a small update to trigger sync
                    pass  # The websocket should auto-sync
                
                if cell_index < len(ydoc._ycells):
                    outputs = ydoc._ycells[cell_index].get("outputs", [])
                    if outputs:
                        logger.info(f"Cell {cell_index} executing... ({elapsed:.1f}s) - {len(outputs)} outputs so far")
            except Exception as e:
                logger.debug(f"Sync attempt failed: {e}")
                pass
        
        result = future.result()
        return result
        
    finally:
        executor.shutdown(wait=False)


# Alternative approach: Create a custom execution function that forces updates
async def __execute_cell_with_forced_sync(notebook, cell_index, kernel, timeout_seconds=300):
    """Execute cell with forced real-time synchronization."""
    start_time = time.time()
    
    # Start execution
    execution_future = asyncio.create_task(
        asyncio.to_thread(notebook.execute_cell, cell_index, kernel)
    )
    
    last_output_count = 0
    
    while not execution_future.done():
        elapsed = time.time() - start_time
        
        if elapsed > timeout_seconds:
            execution_future.cancel()
            try:
                if hasattr(kernel, 'interrupt'):
                    kernel.interrupt()
            except Exception:
                pass
            raise asyncio.TimeoutError(f"Cell execution timed out after {timeout_seconds} seconds")
        
        # Check for new outputs and try to trigger sync
        try:
            ydoc = notebook._doc
            current_outputs = ydoc._ycells[cell_index].get("outputs", [])
            
            if len(current_outputs) > last_output_count:
                last_output_count = len(current_outputs)
                logger.info(f"Cell {cell_index} progress: {len(current_outputs)} outputs after {elapsed:.1f}s")
                
                # Try different sync methods
                try:
                    # Method 1: Force Y-doc update
                    if hasattr(ydoc, 'observe') and hasattr(ydoc, 'unobserve'):
                        # Trigger observers by making a tiny change
                        pass
                        
                    # Method 2: Force websocket message
                    if hasattr(notebook, '_websocket') and notebook._websocket:
                        # The websocket should automatically sync on changes
                        pass
                        
                except Exception as sync_error:
                    logger.debug(f"Sync method failed: {sync_error}")
                    
        except Exception as e:
            logger.debug(f"Output check failed: {e}")
        
        await asyncio.sleep(1)  # Check every second
    
    # Get final result
    try:
        await execution_future
    except asyncio.CancelledError:
        pass
    
    return None


def __is_kernel_busy(kernel):
    """Check if kernel is currently executing something."""
    try:
        # This is a simple check - you might need to adapt based on your kernel client
        if hasattr(kernel, '_client') and hasattr(kernel._client, 'is_alive'):
            return kernel._client.is_alive()
        return False
    except Exception:
        return False


async def __wait_for_kernel_idle(kernel, max_wait_seconds=60):
    """Wait for kernel to become idle before proceeding."""
    start_time = time.time()
    while __is_kernel_busy(kernel):
        elapsed = time.time() - start_time
        if elapsed > max_wait_seconds:
            logger.warning(f"Kernel still busy after {max_wait_seconds}s, proceeding anyway")
            break
        logger.info(f"Waiting for kernel to become idle... ({elapsed:.1f}s)")
        await asyncio.sleep(1)


async def __safe_notebook_operation(operation_func, max_retries=3):
    """Safely execute notebook operations with connection recovery."""
    for attempt in range(max_retries):
        try:
            return await operation_func()
        except Exception as e:
            error_msg = str(e).lower()
            if any(err in error_msg for err in ["websocketclosederror", "connection is already closed", "connection closed"]):
                if attempt < max_retries - 1:
                    logger.warning(f"Connection lost, retrying... (attempt {attempt + 1}/{max_retries})")
                    await asyncio.sleep(1 + attempt)  # Increasing delay
                    continue
                else:
                    logger.error(f"Failed after {max_retries} attempts: {e}")
                    raise Exception(f"Connection failed after {max_retries} retries: {e}")
            else:
                # Non-connection error, don't retry
                raise e
    
    raise Exception("Unexpected error in retry logic")


def _list_notebooks_recursively(server_client, path="", notebooks=None):
    """Recursively list all .ipynb files in the Jupyter server."""
    if notebooks is None:
        notebooks = []
    
    try:
        contents = server_client.contents.list_directory(path)
        for item in contents:
            full_path = f"{path}/{item.name}" if path else item.name
            if item.type == "directory":
                # Recursively search subdirectories
                _list_notebooks_recursively(server_client, full_path, notebooks)
            elif item.type == "notebook" or (item.type == "file" and item.name.endswith('.ipynb')):
                # Add notebook to list without any prefix
                notebooks.append(full_path)
    except Exception as e:
        # If we can't access a directory, just skip it
        pass
    
    return notebooks


def _list_files_recursively(server_client, current_path="", current_depth=0, files=None, max_depth=3):
    """Recursively list all files and directories in the Jupyter server."""
    if files is None:
        files = []
    
    # Stop if we've reached max depth
    if current_depth > max_depth:
        return files
    
    try:
        contents = server_client.contents.list_directory(current_path)
        for item in contents:
            full_path = f"{current_path}/{item.name}" if current_path else item.name
            
            # Format size
            size_str = ""
            if hasattr(item, 'size') and item.size is not None:
                if item.size < 1024:
                    size_str = f"{item.size}B"
                elif item.size < 1024 * 1024:
                    size_str = f"{item.size // 1024}KB"
                else:
                    size_str = f"{item.size // (1024 * 1024)}MB"
            
            # Format last modified
            last_modified = ""
            if hasattr(item, 'last_modified') and item.last_modified:
                last_modified = item.last_modified.strftime("%Y-%m-%d %H:%M:%S")
            
            # Add file/directory to list
            files.append({
                'path': full_path,
                'type': item.type,
                'size': size_str,
                'last_modified': last_modified
            })
            
            # Recursively explore directories
            if item.type == "directory":
                _list_files_recursively(server_client, full_path, current_depth + 1, files, max_depth)
                
    except Exception as e:
        # If we can't access a directory, add an error entry
        files.append({
            'path': current_path or "root",
            'type': "error",
            'size': "",
            'last_modified': f"Error: {str(e)}"
        })
    
    return files

###############################################################################
# Custom Routes.


@mcp.custom_route("/api/connect", ["PUT"])
async def connect(request: Request):
    """Connect to a document and a runtime from the Jupyter MCP server."""

    data = await request.json()
    logger.info("Connecting to document_runtime:", data)

    document_runtime = DocumentRuntime(**data)

    # Clean up existing default notebook if any
    if "default" in notebook_manager:
        try:
            notebook_manager.remove_notebook("default")
        except Exception as e:
            logger.warning(f"Error stopping existing notebook during connect: {e}")

    # Update configuration with new values
    set_config(
        provider=document_runtime.provider,
        runtime_url=document_runtime.runtime_url,
        runtime_id=document_runtime.runtime_id,
        runtime_token=document_runtime.runtime_token,
        document_url=document_runtime.document_url,
        document_id=document_runtime.document_id,
        document_token=document_runtime.document_token
    )

    try:
        __start_kernel()
        return JSONResponse({"success": True})
    except Exception as e:
        logger.error(f"Failed to connect: {e}")
        return JSONResponse({"success": False, "error": str(e)}, status_code=500)


@mcp.custom_route("/api/stop", ["DELETE"])
async def stop(request: Request):
    try:
        current_notebook = notebook_manager.get_current_notebook() or "default"
        if current_notebook in notebook_manager:
            notebook_manager.remove_notebook(current_notebook)
        return JSONResponse({"success": True})
    except Exception as e:
        logger.error(f"Error stopping notebook: {e}")
        return JSONResponse({"success": False, "error": str(e)}, status_code=500)


@mcp.custom_route("/api/healthz", ["GET"])
async def health_check(request: Request):
    """Custom health check endpoint"""
    kernel_status = "unknown"
    try:
        current_notebook = notebook_manager.get_current_notebook() or "default"
        kernel = notebook_manager.get_kernel(current_notebook)
        if kernel:
            kernel_status = "alive" if hasattr(kernel, 'is_alive') and kernel.is_alive() else "dead"
        else:
            kernel_status = "not_initialized"
    except Exception:
        kernel_status = "error"
    return JSONResponse(
        {
            "success": True,
            "service": "jupyter-mcp-server",
            "message": "Jupyter MCP Server is running.",
            "status": "healthy",
            "kernel_status": kernel_status,
        }
    )


###############################################################################
# Tools.
###############################################################################

###############################################################################
# Multi-Notebook Management Tools.


@mcp.tool()
async def connect_notebook(
    notebook_name: str,
    notebook_path: str,
    mode: Literal["connect", "create"] = "connect",
    kernel_id: Optional[str] = None,
) -> str:
    """Connect to a notebook file or create a new one.
    
    Args:
        notebook_name: Unique identifier for the notebook
        notebook_path: Path to the notebook file, relative to the Jupyter server root (e.g. "notebook.ipynb")
        mode: "connect" to connect to existing, "create" to create new
        kernel_id: Specific kernel ID to use (optional, will create new if not provided)
        
    Returns:
        str: Success message with notebook information
    """
    if notebook_name in notebook_manager:
        return f"Notebook '{notebook_name}' is already connected. Use disconnect_notebook first if you want to reconnect."
    
    config = get_config()
    server_client = JupyterServerClient(base_url=config.runtime_url, token=config.runtime_token)

    # Check the Jupyter server
    try:
        server_client.get_status()
    except Exception as e:
        return f"Failed to connect the Jupyter server: {e}"

    # Check the path on Jupyter server
    path = Path(notebook_path)
    try:
        # For relative paths starting with just filename, assume current directory
        parent_path = str(path.parent) if str(path.parent) != "." else ""
        
        if parent_path:
            dir_contents = server_client.contents.list_directory(parent_path)
        else:
            # Check in the root directory of Jupyter server
            dir_contents = server_client.contents.list_directory("")
            
        if mode == "connect":
            file_exists = any(file.name == path.name for file in dir_contents)
            if not file_exists:
                return f"'{notebook_path}' not found in jupyter server, please check the notebook already exists."
    except NotFoundError:
        parent_dir = str(path.parent) if str(path.parent) != "." else "root directory"
        return f"'{parent_dir}' not found in jupyter server, please check the directory path already exists."
    except Exception as e:
        return f"Failed to check the path '{notebook_path}': {e}"

    # Check the kernel
    if kernel_id:
        kernels = server_client.kernels.list_kernels()
        kernel_exists = any(kernel.id == kernel_id for kernel in kernels)
        if not kernel_exists:
            return f"Kernel '{kernel_id}' not found in jupyter server, please check the kernel is already exists."
    
    # Create notebook
    if mode == "create":
        server_client.contents.create_notebook(notebook_path)
    
    # Create kernel client
    kernel = KernelClient(
            server_url=config.runtime_url,
            token=config.runtime_token,
            kernel_id=kernel_id
        )
        
    kernel.start()
        
    # Add notebook to manager
    notebook_manager.add_notebook(
        notebook_name,
        kernel,
        server_url=config.runtime_url,
        token=config.runtime_token,
        path=notebook_path
    )
    notebook_manager.set_current_notebook(notebook_name)
    
    return f"Successfully {'created and ' if mode == 'create' else ''}connected to notebook '{notebook_name}' at path '{notebook_path}'."


@mcp.tool()
async def list_notebook() -> str:
    """List all notebooks in the Jupyter server (including subdirectories) and show which ones are managed.
    
    To interact with a notebook, it has to be "managed". If a notebook is not managed, you can connect to it using the `connect_notebook` tool.
    
    Returns:
        str: TSV formatted table with notebook information including management status
    """
    # Get all notebooks from the Jupyter server
    config = get_config()
    server_client = JupyterServerClient(base_url=config.runtime_url, token=config.runtime_token)
    all_notebooks = _list_notebooks_recursively(server_client)
    
    # Get managed notebooks info
    managed_notebooks = notebook_manager.list_all_notebooks()
    
    if not all_notebooks and not managed_notebooks:
        return "No notebooks found in the Jupyter server."
    
    # Create TSV formatted output
    lines = ["Path\tManaged\tName\tStatus\tCurrent"]
    lines.append("-" * 100)
    
    # Create a set of managed notebook paths for quick lookup
    managed_paths = {info["path"] for info in managed_notebooks.values()}
    
    # Add all notebooks found in the server
    for notebook_path in sorted(all_notebooks):
        is_managed = notebook_path in managed_paths
        
        if is_managed:
            # Find the managed notebook entry
            managed_info = None
            managed_name = None
            for name, info in managed_notebooks.items():
                if info["path"] == notebook_path:
                    managed_info = info
                    managed_name = name
                    break
            
            if managed_info:
                current_marker = "✓" if managed_info["is_current"] else ""
                lines.append(f"{notebook_path}\tYes\t{managed_name}\t{managed_info['kernel_status']}\t{current_marker}")
            else:
                lines.append(f"{notebook_path}\tYes\t-\t-\t")
        else:
            lines.append(f"{notebook_path}\tNo\t-\t-\t")
    
    # Add any managed notebooks that weren't found in the server (edge case)
    for name, info in managed_notebooks.items():
        if info["path"] not in all_notebooks:
            current_marker = "✓" if info["is_current"] else ""
            lines.append(f"{info['path']}\tYes (not found)\t{name}\t{info['kernel_status']}\t{current_marker}")
    
    return "\n".join(lines)


@mcp.tool()
async def restart_notebook(notebook_name: str) -> str:
    """Restart the kernel for a specific notebook.
    
    Args:
        notebook_name: Notebook identifier to restart
        
    Returns:
        str: Success message
    """
    if notebook_name not in notebook_manager:
        return f"Notebook '{notebook_name}' is not connected."
    
    success = notebook_manager.restart_notebook(notebook_name)
    
    if success:
        return f"Notebook '{notebook_name}' kernel restarted successfully. Memory state and imported packages have been cleared."
    else:
        return f"Failed to restart notebook '{notebook_name}'. The kernel may not support restart operation."


@mcp.tool()
async def disconnect_notebook(notebook_name: str) -> str:
    """Disconnect from a specific notebook and release its resources.
    
    Args:
        notebook_name: Notebook identifier to disconnect
        
    Returns:
        str: Success message
    """
    if notebook_name not in notebook_manager:
        return f"Notebook '{notebook_name}' is not connected."
    
    # Get info about which notebook was current
    current_notebook = notebook_manager.get_current_notebook()
    was_current = current_notebook == notebook_name
    
    success = notebook_manager.remove_notebook(notebook_name)
    
    if success:
        message = f"Notebook '{notebook_name}' disconnected successfully."
        
        if was_current:
            new_current = notebook_manager.get_current_notebook()
            if new_current:
                message += f" Current notebook switched to '{new_current}'."
            else:
                message += " No notebooks remaining."
        
        return message
    else:
        return f"Notebook '{notebook_name}' was not found."


@mcp.tool()
async def switch_notebook(notebook_name: str) -> str:
    """Switch the currently active notebook.
    
    Args:
        notebook_name: Notebook identifier to switch to
        
    Returns:
        str: Success message with new active notebook information
    """
    if notebook_name not in notebook_manager:
        available_notebooks = list(notebook_manager.list_all_notebooks().keys())
        if available_notebooks:
            return f"Notebook '{notebook_name}' is not connected. Available notebooks: {', '.join(available_notebooks)}"
        else:
            return f"Notebook '{notebook_name}' is not connected and no notebooks are available."
    
    success = notebook_manager.set_current_notebook(notebook_name)
    
    if success:
        notebooks_info = notebook_manager.list_all_notebooks()
        notebook_info = notebooks_info[notebook_name]
        
        return f"Successfully switched to notebook '{notebook_name}'. Path: '{notebook_info['path']}', Status: {notebook_info['kernel_status']}. All subsequent cell operations will use this notebook."
    else:
        return f"Failed to switch to notebook '{notebook_name}'."

###############################################################################
# Cell Tools.

@mcp.tool()
async def insert_cell(
    cell_index: int,
    cell_type: Literal["code", "markdown"],
    cell_source: str,
) -> str:
    """Insert a cell to specified position.

    Args:
        cell_index: target index for insertion (0-based). Use -1 to append at end.
        cell_type: Type of cell to insert ("code" or "markdown")
        cell_source: Source content for the cell

    Returns:
        str: Success message and the structure of its surrounding cells (up to 5 cells above and 5 cells below)
    """
    async def _insert_cell():
        async with notebook_manager.get_current_connection() as notebook:
            ydoc = notebook._doc
            total_cells = len(ydoc._ycells)
            
            actual_index = cell_index if cell_index != -1 else total_cells
                
            if actual_index < 0 or actual_index > total_cells:
                raise ValueError(
                    f"Cell index {cell_index} is out of range. Notebook has {total_cells} cells. Use -1 to append at end."
                )
            
            if cell_type == "code":
                if actual_index == total_cells:
                    notebook.add_code_cell(cell_source)
                else:
                    notebook.insert_code_cell(actual_index, cell_source)
            elif cell_type == "markdown":
                if actual_index == total_cells:
                    notebook.add_markdown_cell(cell_source)
                else:
                    notebook.insert_markdown_cell(actual_index, cell_source)
            
            # Get surrounding cells info
            new_total_cells = len(ydoc._ycells)
            surrounding_info = get_surrounding_cells_info(notebook, actual_index, new_total_cells)
            
            return f"Cell inserted successfully at index {actual_index} ({cell_type})!\n\nCurrent Surrounding Cells:\n{surrounding_info}"
    
    return await __safe_notebook_operation(_insert_cell)


@mcp.tool()
async def insert_execute_code_cell(cell_index: int, cell_source: str) -> list[Union[str, ImageContent]]:
    """Insert and execute a code cell in a Jupyter notebook.

    Args:
        cell_index: Index of the cell to insert (0-based). Use -1 to append at end and execute.
        cell_source: Code source

    Returns:
        list[Union[str, ImageContent]]: List of outputs from the executed cell
    """
    async def _insert_execute():
        kernel = __ensure_kernel_alive()
        async with notebook_manager.get_current_connection() as notebook:
            ydoc = notebook._doc
            total_cells = len(ydoc._ycells)
            
            actual_index = cell_index if cell_index != -1 else total_cells
                
            if actual_index < 0 or actual_index > total_cells:
                raise ValueError(
                    f"Cell index {cell_index} is out of range. Notebook has {total_cells} cells. Use -1 to append at end."
                )
            
            if actual_index == total_cells:
                notebook.add_code_cell(cell_source)
            else:
                notebook.insert_code_cell(actual_index, cell_source)
                
            notebook.execute_cell(actual_index, kernel)

            ydoc = notebook._doc
            outputs = ydoc._ycells[actual_index]["outputs"]
            return safe_extract_outputs(outputs)
    
    return await __safe_notebook_operation(_insert_execute)


@mcp.tool()
async def overwrite_cell_source(cell_index: int, cell_source: str) -> str:
    """Overwrite the source of an existing cell.
       Note this does not execute the modified cell by itself.

    Args:
        cell_index: Index of the cell to overwrite (0-based)
        cell_source: New cell source - must match existing cell type

    Returns:
        str: Success message with diff showing changes made
    """
    async def _overwrite_cell():
        async with notebook_manager.get_current_connection() as notebook:
            ydoc = notebook._doc
            
            if cell_index < 0 or cell_index >= len(ydoc._ycells):
                raise ValueError(
                    f"Cell index {cell_index} is out of range. Notebook has {len(ydoc._ycells)} cells."
                )
            
            # Get original cell content
            old_source_raw = ydoc._ycells[cell_index].get("source", "")
            
            # Convert source to string if it's a list (which is common in notebooks)
            if isinstance(old_source_raw, list):
                old_source = "".join(old_source_raw)
            else:
                old_source = str(old_source_raw)
            
            # Set new cell content
            notebook.set_cell_source(cell_index, cell_source)
            
            # Generate diff
            old_lines = old_source.splitlines(keepends=False)
            new_lines = cell_source.splitlines(keepends=False)
            
            diff_lines = list(difflib.unified_diff(
                old_lines, 
                new_lines, 
                lineterm='',
                n=3  # Number of context lines
            ))
            
            # Remove the first 3 lines (file headers) from unified_diff output
            if len(diff_lines) > 3:
                diff_content = '\n'.join(diff_lines[3:])
            else:
                diff_content = "no changes detected"
            
            if not diff_content.strip():
                return f"Cell {cell_index} overwritten successfully - no changes detected"
            
            return f"Cell {cell_index} overwritten successfully!\n\n```diff\n{diff_content}\n```"
    
    return await __safe_notebook_operation(_overwrite_cell)

@mcp.tool()
async def execute_cell_with_progress(cell_index: int, timeout_seconds: int = 300) -> list[Union[str, ImageContent]]:
    """Execute a specific cell with timeout and progress monitoring.
    Args:
        cell_index: Index of the cell to execute (0-based)
        timeout_seconds: Maximum time to wait for execution (default: 300s)
    Returns:
        list[Union[str, ImageContent]]: List of outputs from the executed cell
    """
    async def _execute():
        kernel = __ensure_kernel_alive()
        await __wait_for_kernel_idle(kernel, max_wait_seconds=30)
        
        async with notebook_manager.get_current_connection() as notebook:
            ydoc = notebook._doc

            if cell_index < 0 or cell_index >= len(ydoc._ycells):
                raise ValueError(
                    f"Cell index {cell_index} is out of range. Notebook has {len(ydoc._ycells)} cells."
                )

            logger.info(f"Starting execution of cell {cell_index} with {timeout_seconds}s timeout")
            
            try:
                # Use the corrected timeout function
                await __execute_cell_with_forced_sync(notebook, cell_index, kernel, timeout_seconds)

                # Get final outputs
                ydoc = notebook._doc
                outputs = ydoc._ycells[cell_index]["outputs"]
                result = safe_extract_outputs(outputs)
                
                logger.info(f"Cell {cell_index} completed successfully with {len(result)} outputs")
                return result
                
            except asyncio.TimeoutError as e:
                logger.error(f"Cell {cell_index} execution timed out: {e}")
                try:
                    if kernel and hasattr(kernel, 'interrupt'):
                        kernel.interrupt()
                        logger.info("Sent interrupt signal to kernel")
                except Exception as interrupt_err:
                    logger.error(f"Failed to interrupt kernel: {interrupt_err}")
                
                # Return partial outputs if available
                try:
                    outputs = ydoc._ycells[cell_index].get("outputs", [])
                    partial_outputs = safe_extract_outputs(outputs)
                    partial_outputs.append(f"[TIMEOUT ERROR: Execution exceeded {timeout_seconds} seconds]")
                    return partial_outputs
                except Exception:
                    pass
                
                return [f"[TIMEOUT ERROR: Cell execution exceeded {timeout_seconds} seconds and was interrupted]"]
                
            except Exception as e:
                logger.error(f"Error executing cell {cell_index}: {e}")
                raise
    
    return await __safe_notebook_operation(_execute, max_retries=1)

# Simpler real-time monitoring without forced sync
@mcp.tool()
async def execute_cell_simple_timeout(cell_index: int, timeout_seconds: int = 300) -> list[Union[str, ImageContent]]:
    """Execute a cell with simple timeout (no forced real-time sync). To be used for short-running cells.
    This won't force real-time updates but will work reliably.
    """
    async def _execute():
        kernel = __ensure_kernel_alive()
        await __wait_for_kernel_idle(kernel, max_wait_seconds=30)
        
        async with notebook_manager.get_current_connection() as notebook:
            ydoc = notebook._doc
            if cell_index < 0 or cell_index >= len(ydoc._ycells):
                raise ValueError(f"Cell index {cell_index} is out of range.")

            logger.info(f"Starting execution of cell {cell_index} with {timeout_seconds}s timeout")
            
            # Simple execution with timeout
            execution_task = asyncio.create_task(
                asyncio.to_thread(notebook.execute_cell, cell_index, kernel)
            )
            
            try:
                await asyncio.wait_for(execution_task, timeout=timeout_seconds)
            except asyncio.TimeoutError:
                execution_task.cancel()
                if kernel and hasattr(kernel, 'interrupt'):
                    kernel.interrupt()
                return [f"[TIMEOUT ERROR: Cell execution exceeded {timeout_seconds} seconds]"]

            # Get final outputs
            outputs = ydoc._ycells[cell_index]["outputs"]
            result = safe_extract_outputs(outputs)
            
            logger.info(f"Cell {cell_index} completed successfully")
            return result
    
    return await __safe_notebook_operation(_execute, max_retries=1)


@mcp.tool()
async def execute_cell_streaming(cell_index: int, timeout_seconds: int = 300, progress_interval: int = 5) -> list[Union[str, ImageContent]]:
    """Execute cell with streaming progress updates. To be used for long-running cells.
    Args:
        cell_index: Index of the cell to execute (0-based)
        timeout_seconds: Maximum time to wait for execution (default: 300s)  
        progress_interval: Seconds between progress updates (default: 5s)
    Returns:
        list[Union[str, ImageContent]]: List of outputs including progress updates
    """
    async def _execute_streaming():
        kernel = __ensure_kernel_alive()
        await __wait_for_kernel_idle(kernel, max_wait_seconds=30)
        
        outputs_log = []
        
        async with notebook_manager.get_current_connection() as notebook:
            ydoc = notebook._doc
            if cell_index < 0 or cell_index >= len(ydoc._ycells):
                raise ValueError(f"Cell index {cell_index} is out of range.")

            # Start execution in background
            execution_task = asyncio.create_task(
                asyncio.to_thread(notebook.execute_cell, cell_index, kernel)
            )
            
            start_time = time.time()
            last_output_count = 0
            
            # Monitor progress
            while not execution_task.done():
                elapsed = time.time() - start_time
                
                # Check timeout
                if elapsed > timeout_seconds:
                    execution_task.cancel()
                    outputs_log.append(f"[TIMEOUT at {elapsed:.1f}s: Cancelling execution]")
                    try:
                        kernel.interrupt()
                        outputs_log.append("[Sent interrupt signal to kernel]")
                    except Exception:
                        pass
                    break
                
                # Check for new outputs
                try:
                    current_outputs = ydoc._ycells[cell_index].get("outputs", [])
                    if len(current_outputs) > last_output_count:
                        new_outputs = current_outputs[last_output_count:]
                        for output in new_outputs:
                            extracted = extract_output(output)
                            if extracted.strip():
                                outputs_log.append(f"[{elapsed:.1f}s] {extracted}")
                        last_output_count = len(current_outputs)
                
                except Exception as e:
                    outputs_log.append(f"[{elapsed:.1f}s] Error checking outputs: {e}")
                
                # Progress update
                if int(elapsed) % progress_interval == 0 and elapsed > 0:
                    outputs_log.append(f"[PROGRESS: {elapsed:.1f}s elapsed, {last_output_count} outputs so far]")
                
                await asyncio.sleep(1)
            
            # Get final result
            if not execution_task.cancelled():
                try:
                    await execution_task
                    final_outputs = ydoc._ycells[cell_index].get("outputs", [])
                    outputs_log.append(f"[COMPLETED in {time.time() - start_time:.1f}s]")
                    
                    # Add any final outputs not captured during monitoring
                    if len(final_outputs) > last_output_count:
                        remaining = final_outputs[last_output_count:]
                        for output in remaining:
                            extracted = extract_output(output)
                            if extracted.strip():
                                outputs_log.append(extracted)
                                
                except Exception as e:
                    outputs_log.append(f"[ERROR: {e}]")
            
            return outputs_log if outputs_log else ["[No output generated]"]
    
    return await __safe_notebook_operation(_execute_streaming, max_retries=1)

@mcp.tool()
async def read_all_cells() -> list[dict[str, Union[str, int, list[Union[str, ImageContent]]]]]:
    """Read all cells from the Jupyter notebook.
    Returns:
        list[dict]: List of cell information including index, type, source,
                    and outputs (for code cells)
    """
    async def _read_all():
        async with notebook_manager.get_current_connection() as notebook:
            ydoc = notebook._doc
            cells = []

            for i, cell in enumerate(ydoc._ycells):
                cells.append(CellInfo.from_cell(i, cell).model_dump(exclude_none=True))
            return cells
    
    return await __safe_notebook_operation(_read_all)


@mcp.tool()
async def list_cell() -> str:
    """List the basic information of all cells in the notebook.
    
    Returns a formatted table showing the index, type, execution count (for code cells),
    and first line of each cell. This provides a quick overview of the notebook structure
    and is useful for locating specific cells for operations like delete or insert.
    
    Returns:
        str: Formatted table with cell information (Index, Type, Count, First Line)
    """
    async def _list_cells():
        async with notebook_manager.get_current_connection() as notebook:
            ydoc = notebook._doc
            return format_cell_list(ydoc._ycells)
    
    return await __safe_notebook_operation(_list_cells)


@mcp.tool()
async def read_cell(cell_index: int) -> dict[str, Union[str, int, list[Union[str, ImageContent]]]]:
    """Read a specific cell from the Jupyter notebook.
    Args:
        cell_index: Index of the cell to read (0-based)
    Returns:
        dict: Cell information including index, type, source, and outputs (for code cells)
    """
    async def _read_cell():
        async with notebook_manager.get_current_connection() as notebook:
            ydoc = notebook._doc

            if cell_index < 0 or cell_index >= len(ydoc._ycells):
                raise ValueError(
                    f"Cell index {cell_index} is out of range. Notebook has {len(ydoc._ycells)} cells."
                )

            cell = ydoc._ycells[cell_index]
            return CellInfo.from_cell(cell_index=cell_index, cell=cell).model_dump(exclude_none=True)
    
    return await __safe_notebook_operation(_read_cell)

@mcp.tool()
async def delete_cell(cell_index: int) -> str:
    """Delete a specific cell from the Jupyter notebook.
    Args:
        cell_index: Index of the cell to delete (0-based)
    Returns:
        str: Success message
    """
    async def _delete_cell():
        async with notebook_manager.get_current_connection() as notebook:
            ydoc = notebook._doc

            if cell_index < 0 or cell_index >= len(ydoc._ycells):
                raise ValueError(
                    f"Cell index {cell_index} is out of range. Notebook has {len(ydoc._ycells)} cells."
                )

            cell_type = ydoc._ycells[cell_index].get("cell_type", "unknown")

            # Delete the cell
            del ydoc._ycells[cell_index]

            return f"Cell {cell_index} ({cell_type}) deleted successfully."
    
    return await __safe_notebook_operation(_delete_cell)


@mcp.tool()
async def execute_ipython(code: str, timeout: int = 60) -> list[Union[str, ImageContent]]:
    """Execute IPython code directly in the kernel on the current active notebook.
    
    This powerful tool supports:
    1. Magic commands (e.g., %timeit, %who, %load, %run, %matplotlib)
    2. Shell commands (e.g., !pip install, !ls, !cat)
    3. Python code (e.g., print(df.head()), df.info())
    
    Use cases:
    - Performance profiling and debugging
    - Environment exploration and package management
    - Variable inspection and data analysis
    - File system operations on Jupyter server
    - Temporary calculations and quick tests

    Args:
        code: IPython code to execute (supports magic commands, shell commands with !, and Python code)
        timeout: Execution timeout in seconds (default: 60s)
    Returns:
        List of outputs from the executed code
    """
    async def _execute_ipython():
        # Get current notebook name and kernel
        current_notebook = notebook_manager.get_current_notebook() or "default"
        kernel = notebook_manager.get_kernel(current_notebook)
        
        if not kernel:
            # Ensure kernel is alive
            kernel = __ensure_kernel_alive()
        
        # Wait for kernel to be idle before executing
        await __wait_for_kernel_idle(kernel, max_wait_seconds=30)
        
        logger.info(f"Executing IPython code with timeout {timeout}s: {code[:100]}...")
        
        try:
            # Execute code directly with kernel
            execution_task = asyncio.create_task(
                asyncio.to_thread(kernel.execute, code)
            )
            
            # Wait for execution with timeout
            try:
                outputs = await asyncio.wait_for(execution_task, timeout=timeout)
            except asyncio.TimeoutError:
                execution_task.cancel()
                try:
                    if kernel and hasattr(kernel, 'interrupt'):
                        kernel.interrupt()
                        logger.info("Sent interrupt signal to kernel due to timeout")
                except Exception as interrupt_err:
                    logger.error(f"Failed to interrupt kernel: {interrupt_err}")
                
                return [f"[TIMEOUT ERROR: IPython execution exceeded {timeout} seconds and was interrupted]"]
            
            # Process and extract outputs
            if outputs:
                result = safe_extract_outputs(outputs['outputs'])
                logger.info(f"IPython execution completed successfully with {len(result)} outputs")
                return result
            else:
                return ["[No output generated]"]
                
        except Exception as e:
            logger.error(f"Error executing IPython code: {e}")
            return [f"[ERROR: {str(e)}]"]
    
    return await __safe_notebook_operation(_execute_ipython, max_retries=1)


@mcp.tool()
async def list_all_files(path: str = "", max_depth: int = 3) -> str:
    """List all files and directories in the Jupyter server's file system.
    
    This tool recursively lists files and directories from the Jupyter server's content API,
    showing the complete file structure including notebooks, data files, scripts, and directories.
    
    Args:
        path: The starting path to list from (empty string means root directory)
        max_depth: Maximum depth to recurse into subdirectories (default: 3)
        
    Returns:
        str: Tab-separated table with columns: Path, Type, Size, Last_Modified
    """
    async def _list_all_files():
        config = get_config()
        server_client = JupyterServerClient(base_url=config.runtime_url, token=config.runtime_token)
        
        # Get all files starting from the specified path using the utility function
        all_files = _list_files_recursively(server_client, path, 0, None, max_depth)
        
        if not all_files:
            return f"No files found in path '{path or 'root'}'"
        
        # Sort files by path for better readability
        all_files.sort(key=lambda x: x['path'])
        
        # Create TSV formatted output
        lines = ["Path\tType\tSize\tLast_Modified"]
        for file_info in all_files:
            lines.append(f"{file_info['path']}\t{file_info['type']}\t{file_info['size']}\t{file_info['last_modified']}")
        
        return "\n".join(lines)
    
    return await __safe_notebook_operation(_list_all_files)


@mcp.tool()
async def list_kernel() -> str:
    """List all available kernels in the Jupyter server.
    
    This tool shows all running and available kernel sessions on the Jupyter server,
    including their IDs, names, states, connection information, and kernel specifications.
    Useful for monitoring kernel resources and identifying specific kernels for connection.
    
    Returns:
        str: Tab-separated table with columns: ID, Name, Display_Name, Language, State, Connections, Last_Activity, Environment
    """
    async def _list_kernels():
        config = get_config()
        server_client = JupyterServerClient(base_url=config.runtime_url, token=config.runtime_token)
        
        try:
            # Get all kernels from the Jupyter server
            kernels = server_client.kernels.list_kernels()
            
            if not kernels:
                return "No kernels found on the Jupyter server."
            
            # Get kernel specifications for additional details
            kernels_specs = server_client.kernelspecs.list_kernelspecs()
            
            # Create enhanced kernel information list
            output = []
            for kernel in kernels:
                kernel_info = {
                    "id": kernel.id or "unknown",
                    "name": kernel.name or "unknown",
                    "state": "unknown",
                    "connections": "unknown", 
                    "last_activity": "unknown",
                    "display_name": "unknown",
                    "language": "unknown",
                    "env": "unknown"
                }
                
                # Get kernel state - this might vary depending on the API version
                if hasattr(kernel, 'execution_state'):
                    kernel_info["state"] = kernel.execution_state
                elif hasattr(kernel, 'state'):
                    kernel_info["state"] = kernel.state
                
                # Get connection count
                if hasattr(kernel, 'connections'):
                    kernel_info["connections"] = str(kernel.connections)
                
                # Get last activity
                if hasattr(kernel, 'last_activity') and kernel.last_activity:
                    if hasattr(kernel.last_activity, 'strftime'):
                        kernel_info["last_activity"] = kernel.last_activity.strftime("%Y-%m-%d %H:%M:%S")
                    else:
                        kernel_info["last_activity"] = str(kernel.last_activity)
                
                output.append(kernel_info)
            
            # Enhance kernel info with specifications
            for kernel in output:
                kernel_name = kernel["name"]
                if hasattr(kernels_specs, 'kernelspecs') and kernel_name in kernels_specs.kernelspecs:
                    kernel_spec = kernels_specs.kernelspecs[kernel_name]
                    if hasattr(kernel_spec, 'spec'):
                        if hasattr(kernel_spec.spec, 'display_name'):
                            kernel["display_name"] = kernel_spec.spec.display_name
                        if hasattr(kernel_spec.spec, 'language'):
                            kernel["language"] = kernel_spec.spec.language
                        if hasattr(kernel_spec.spec, 'env'):
                            # Convert env dict to a readable string format
                            env_dict = kernel_spec.spec.env
                            if env_dict:
                                env_str = "; ".join([f"{k}={v}" for k, v in env_dict.items()])
                                kernel["env"] = env_str[:100] + "..." if len(env_str) > 100 else env_str
            
            # Create TSV formatted output
            lines = ["ID\tName\tDisplay_Name\tLanguage\tState\tConnections\tLast_Activity\tEnvironment"]
            
            for kernel in output:
                lines.append(f"{kernel['id']}\t{kernel['name']}\t{kernel['display_name']}\t{kernel['language']}\t{kernel['state']}\t{kernel['connections']}\t{kernel['last_activity']}\t{kernel['env']}")
            
            return "\n".join(lines)
            
        except Exception as e:
            return f"Error listing kernels: {str(e)}"
    
    return await __safe_notebook_operation(_list_kernels)


###############################################################################
# Commands.


@click.group()
def server():
    """Manages Jupyter MCP Server."""
    pass


@server.command("connect")
@click.option(
    "--provider",
    envvar="PROVIDER",
    type=click.Choice(["jupyter", "datalayer"]),
    default="jupyter",
    help="The provider to use for the document and runtime. Defaults to 'jupyter'.",
)
@click.option(
    "--runtime-url",
    envvar="RUNTIME_URL",
    type=click.STRING,
    default="http://localhost:8888",
    help="The runtime URL to use. For the jupyter provider, this is the Jupyter server URL. For the datalayer provider, this is the Datalayer runtime URL.",
)
@click.option(
    "--runtime-id",
    envvar="RUNTIME_ID",
    type=click.STRING,
    default=None,
    help="The kernel ID to use. If not provided, a new kernel should be started.",
)
@click.option(
    "--runtime-token",
    envvar="RUNTIME_TOKEN",
    type=click.STRING,
    default=None,
    help="The runtime token to use for authentication with the provider.  For the jupyter provider, this is the jupyter token. For the datalayer provider, this is the datalayer token. If not provided, the provider should accept anonymous requests.",
)
@click.option(
    "--document-url",
    envvar="DOCUMENT_URL",
    type=click.STRING,
    default="http://localhost:8888",
    help="The document URL to use. For the jupyter provider, this is the Jupyter server URL. For the datalayer provider, this is the Datalayer document URL.",
)
@click.option(
    "--document-id",
    envvar="DOCUMENT_ID",
    type=click.STRING,
    default="notebook.ipynb",
    help="The document id to use. For the jupyter provider, this is the notebook path. For the datalayer provider, this is the notebook path.",
)
@click.option(
    "--document-token",
    envvar="DOCUMENT_TOKEN",
    type=click.STRING,
    default=None,
    help="The document token to use for authentication with the provider. For the jupyter provider, this is the jupyter token. For the datalayer provider, this is the datalayer token. If not provided, the provider should accept anonymous requests.",
)
@click.option(
    "--jupyter-mcp-server-url",
    envvar="JUPYTER_MCP_SERVER_URL",
    type=click.STRING,
    default="http://localhost:4040",
    help="The URL of the Jupyter MCP Server to connect to. Defaults to 'http://localhost:4040'.",
)
def connect_command(
    jupyter_mcp_server_url: str,
    runtime_url: str,
    runtime_id: str,
    runtime_token: str,
    document_url: str,
    document_id: str,
    document_token: str,
    provider: str,
):
    """Command to connect a Jupyter MCP Server to a document and a runtime."""

    # Set configuration using the singleton
    set_config(
        provider=provider,
        runtime_url=runtime_url,
        runtime_id=runtime_id,
        runtime_token=runtime_token,
        document_url=document_url,
        document_id=document_id,
        document_token=document_token
    )

    config = get_config()
    
    document_runtime = DocumentRuntime(
        provider=config.provider,
        runtime_url=config.runtime_url,
        runtime_id=config.runtime_id,
        runtime_token=config.runtime_token,
        document_url=config.document_url,
        document_id=config.document_id,
        document_token=config.document_token,
    )

    r = httpx.put(
        f"{jupyter_mcp_server_url}/api/connect",
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
        content=document_runtime.model_dump_json(),
    )
    r.raise_for_status()


@server.command("stop")
@click.option(
    "--jupyter-mcp-server-url",
    envvar="JUPYTER_MCP_SERVER_URL",
    type=click.STRING,
    default="http://localhost:4040",
    help="The URL of the Jupyter MCP Server to stop. Defaults to 'http://localhost:4040'.",
)
def stop_command(jupyter_mcp_server_url: str):
    r = httpx.delete(
        f"{jupyter_mcp_server_url}/api/stop",
    )
    r.raise_for_status()


@server.command("start")
@click.option(
    "--transport",
    envvar="TRANSPORT",
    type=click.Choice(["stdio", "streamable-http"]),
    default="stdio",
    help="The transport to use for the MCP server. Defaults to 'stdio'.",
)
@click.option(
    "--provider",
    envvar="PROVIDER",
    type=click.Choice(["jupyter", "datalayer"]),
    default="jupyter",
    help="The provider to use for the document and runtime. Defaults to 'jupyter'.",
)
@click.option(
    "--runtime-url",
    envvar="RUNTIME_URL",
    type=click.STRING,
    default="http://localhost:8888",
    help="The runtime URL to use. For the jupyter provider, this is the Jupyter server URL. For the datalayer provider, this is the Datalayer runtime URL.",
)
@click.option(
    "--start-new-runtime",
    envvar="START_NEW_RUNTIME",
    type=click.BOOL,
    default=True,
    help="Start a new runtime or use an existing one.",
)
@click.option(
    "--runtime-id",
    envvar="RUNTIME_ID",
    type=click.STRING,
    default=None,
    help="The kernel ID to use. If not provided, a new kernel should be started.",
)
@click.option(
    "--runtime-token",
    envvar="RUNTIME_TOKEN",
    type=click.STRING,
    default=None,
    help="The runtime token to use for authentication with the provider. If not provided, the provider should accept anonymous requests.",
)
@click.option(
    "--document-url",
    envvar="DOCUMENT_URL",
    type=click.STRING,
    default="http://localhost:8888",
    help="The document URL to use. For the jupyter provider, this is the Jupyter server URL. For the datalayer provider, this is the Datalayer document URL.",
)
@click.option(
    "--document-id",
    envvar="DOCUMENT_ID",
    type=click.STRING,
    default="notebook.ipynb",
    help="The document id to use. For the jupyter provider, this is the notebook path. For the datalayer provider, this is the notebook path.",
)
@click.option(
    "--document-token",
    envvar="DOCUMENT_TOKEN",
    type=click.STRING,
    default=None,
    help="The document token to use for authentication with the provider. If not provided, the provider should accept anonymous requests.",
)
@click.option(
    "--port",
    envvar="PORT",
    type=click.INT,
    default=4040,
    help="The port to use for the Streamable HTTP transport. Ignored for stdio transport.",
)
def start_command(
    transport: str,
    start_new_runtime: bool,
    runtime_url: str,
    runtime_id: str,
    runtime_token: str,
    document_url: str,
    document_id: str,
    document_token: str,
    port: int,
    provider: str,
):
    """Start the Jupyter MCP server with a transport."""

    # Set configuration using the singleton
    config = set_config(
        transport=transport,
        provider=provider,
        runtime_url=runtime_url,
        start_new_runtime=start_new_runtime,
        runtime_id=runtime_id,
        runtime_token=runtime_token,
        document_url=document_url,
        document_id=document_id,
        document_token=document_token,
        port=port
    )

    if config.start_new_runtime or config.runtime_id:
        try:
            __start_kernel()
        except Exception as e:
            logger.error(f"Failed to start kernel on startup: {e}")

    logger.info(f"Starting Jupyter MCP Server with transport: {transport}")

    if transport == "stdio":
        mcp.run(transport="stdio")
    elif transport == "streamable-http":
        uvicorn.run(mcp.streamable_http_app, host="0.0.0.0", port=port)  # noqa: S104
    else:
        raise Exception("Transport should be `stdio` or `streamable-http`.")


###############################################################################
# Main.


if __name__ == "__main__":
    start_command()