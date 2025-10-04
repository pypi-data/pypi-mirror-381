"""
Ultra-simplified parallel execution for scriptthing.

Uses common format module and enhanced Executable with unified execution path.
"""

import os
from concurrent.futures import ProcessPoolExecutor, as_completed
from typing import Iterator, Dict, Any, Optional
from jinja2 import Template

from scriptthing.utils.pretty import Print
from ..shell.script_wrapper import Executable
from ..formats import create_items_for_parallel


def stream(
    template: str,
    input_data: str,
    chunk_size: Optional[int] = None,
    workers: Optional[int] = None,
    separator: Optional[str] = None,
    _print: bool = False
) -> Iterator[str]:
    """
    Stream parallel execution - ultra-simplified.
    
    Uses common format module and enhanced Executable.
    """
    if workers is None:
        workers = os.cpu_count() or 4
    
    # Create items using common format module
    items = create_items_for_parallel(input_data, chunk_size, separator)

    if _print:
        for (_, fields) in items:
            cmd = _render_item(template, fields)
            Print.plain(cmd)
        exit(0)
    
    # Execute in parallel using enhanced Executable
    with ProcessPoolExecutor(max_workers=workers) as executor:
        futures = [
            executor.submit(_execute_item, template, data, fields)
            for data, fields in items
        ]
        
        # Stream results as they complete
        for future in as_completed(futures):
            try:
                result = future.result()
                # Yield stdout if present
                if result and result.text.strip():
                    yield result.text.strip()
                # Yield stderr if present (prefixed to distinguish from stdout)
                if result and result.stderr_text.strip():
                    yield f"STDERR: {result.stderr_text.strip()}"
            except Exception as e:
                yield f"ERROR: {e}"

def _render_item(template: str, fields: Dict[str, Any]):
    # Render template
    try:
        if '{{' in template:
            command = Template(template).render(**fields)
        else:
            command = template.format(**fields)
    except Exception:
        command = template
    return command


def _execute_item(template: str, data: str, fields: Dict[str, Any]) -> Any:
    """Execute item using enhanced Executable (unified path)."""
    command = _render_item(template, fields)
    # Use enhanced Executable - it handles everything automatically!
    executable = Executable()  # No path needed - auto-determined from command
    return executable(command, stdin_input=data)
