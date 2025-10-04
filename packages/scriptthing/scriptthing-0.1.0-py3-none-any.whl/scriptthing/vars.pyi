"""
Type stubs for scriptthing variables.

This file provides IDE support for variable imports and is compatible with:
- pyright (Pylance, Vim/Neovim)
- python-lsp-server (pylsp)
- mypy
- Other Python LSP implementations

Auto-generated - do not edit manually.
Regenerate with: scriptthing vars generate-bindings
"""

from typing import Any, Optional
from datetime import timedelta

# Variable declarations
ST_DEFAULT_REPO: str

# Function signatures
def refresh() -> None:
    """Refresh variable bindings from store."""
    ...

def get(key: str, default: Any = ...) -> Any:
    """Get a variable value with optional default."""
    ...

def put(key: str, value: Any, ttl: Optional[timedelta] = ...) -> None:
    """Store a variable with optional TTL."""
    ...

def delete(key: str) -> None:
    """Delete a variable."""
    ...

def show_all() -> dict[str, dict[str, Any]]:
    """Get all stored variables with metadata."""
    ...

# Module-level attributes for LSP compatibility
__all__: list[str]

# Explicit exports for LSP autocompletion
__all__ = ['ST_DEFAULT_REPO', 'refresh', 'get', 'put', 'delete', 'show_all']
