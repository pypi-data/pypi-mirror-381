"""
Static variable bindings for scriptthing variables.

This module provides static access to scriptthing variables stored in the store.
Variables can be accessed as attributes:

    from scriptthing.vars import NAMESPACE
    # equivalent to: from scriptthing import store; store.get("NAMESPACE")

The module dynamically loads variables from the store and provides them as attributes.
"""

from typing import Any
from .utils import store
import sys


def _infer_type_hint(value):
    """Infer type hint for a value, with smart container type inference."""
    if value is None:
        return "None"
    
    # Handle primitive types
    type_name = type(value).__name__
    if type_name in ('bool', 'str', 'int', 'float', 'complex', 'bytes', 'bytearray'):
        return type_name
    
    # Handle containers with element type inference
    if isinstance(value, (list, set, frozenset)):
        if not value:
            return f"{type_name}[Any]"
        
        # Check if all elements have the same type
        element_types = {type(item).__name__ for item in value}
        if len(element_types) == 1:
            # All elements are the same type, infer from any element
            element_type = _infer_type_hint(next(iter(value)))
            return f"{type_name}[{element_type}]"
        return f"{type_name}[Any]"
    
    elif isinstance(value, tuple):
        if not value:
            return "tuple[()]"
        elif len(value) <= 5:  # Show exact types for small tuples
            element_types = [_infer_type_hint(item) for item in value]
            return f"tuple[{', '.join(element_types)}]"
        return "tuple[Any, ...]"
    
    elif isinstance(value, dict):
        if not value:
            return "dict[Any, Any]"
        
        # Infer key and value types
        key_types = {type(k).__name__ for k in value.keys()}
        val_types = {type(v).__name__ for v in value.values()}
        
        if len(key_types) == 1 and len(val_types) == 1:
            key_type = _infer_type_hint(next(iter(value.keys())))
            val_type = _infer_type_hint(next(iter(value.values())))
            return f"dict[{key_type}, {val_type}]"
        return "dict[Any, Any]"
    
    # Handle class instances
    module_name = type(value).__module__
    if module_name in ('builtins', '__main__') or module_name.startswith('_'):
        return type_name
    return f"{module_name}.{type_name}"


def __getattr__(name: str) -> Any:
    """
    Dynamically provide access to stored variables as module attributes.
    
    This allows importing variables directly:
        from scriptthing.vars import VARIABLE_NAME
    
    Which is equivalent to:
        from scriptthing import store
        store.get("VARIABLE_NAME")
    """
    try:
        return store.get(name)
    except KeyError:
        raise AttributeError(f"Variable '{name}' not found in scriptthing store. "
                           f"Use 'scriptthing vars show' to see available variables.")


def __dir__():
    """
    Return a list of all available variable names for tab completion and introspection.
    """
    try:
        variables = store._get_all()
        # Include both dynamically loaded vars and module functions
        base_attrs = ['refresh', 'get', 'put', 'delete', 'show_all']
        return base_attrs + [name for name in variables.keys() if name.isidentifier()]
    except Exception:
        return ['refresh', 'get', 'put', 'delete', 'show_all']


def refresh():
    """
    Refresh function for API compatibility.
    Since variables are accessed dynamically via __getattr__, no action is needed.
    This function exists for backward compatibility and explicit refresh requests.
    """
    pass  # Dynamic access via __getattr__ means no refresh needed


def _auto_generate_bindings_if_enabled():
    """
    Automatically generate IDE binding files if auto-generation is enabled.
    This runs silently in the background when variables are modified.
    """
    try:
        from .config.config import get_auto_generate_bindings
        
        if not get_auto_generate_bindings():
            return  # Auto-generation is disabled
        
        # Generate IDE support files silently
        from pathlib import Path
        
        # Generate stub file (.pyi) - this is all we need for IDE support
        stub_content = _generate_stub_file()
        stub_file = Path(__file__).parent / "vars.pyi"
        with stub_file.open("w") as f:
            f.write(stub_content)
        
        # Dynamic access via __getattr__ handles all variable access
        
    except Exception:
        # Fail silently - don't break variable operations if binding generation fails
        pass





def _generate_stub_file():
    """
    Generate a .pyi stub file for IDE support.
    This provides type hints and variable declarations that IDEs can detect.
    Optimized for LSP compatibility (pyright, pylsp, etc.)
    """
    try:
        variables = store._get_all()
        
        lines = [
            '"""',
            'Type stubs for scriptthing variables.',
            '',
            'This file provides IDE support for variable imports and is compatible with:',
            '- pyright (Pylance, Vim/Neovim)',
            '- python-lsp-server (pylsp)',
            '- mypy',
            '- Other Python LSP implementations',
            '',
            'Auto-generated - do not edit manually.',
            'Regenerate with: scriptthing vars generate-bindings',
            '"""',
            '',
            'from typing import Any, Optional',
            'from datetime import timedelta',
            '',
        ]
        
        if not variables:
            lines.extend([
                "# No variables currently stored",
                "# Use 'scriptthing vars set KEY value' to add variables",
                "",
            ])
        else:
            lines.append("# Variable declarations")
            for var_name in sorted(variables.keys()):
                if var_name.isidentifier():
                    # Try to infer better types based on the actual value
                    var_data = variables[var_name]
                    actual_value = var_data.get('value')
                    
                    type_hint = _infer_type_hint(actual_value)
                    
                    lines.append(f'{var_name}: {type_hint}')
                else:
                    lines.append(f'# Skipped {var_name} (invalid Python identifier)')
            
            lines.append("")
        
        # Add function signatures with proper typing
        lines.extend([
            "# Function signatures",
            "def refresh() -> None:",
            "    \"\"\"Refresh variable bindings from store.\"\"\"",
            "    ...",
            "",
            "def get(key: str, default: Any = ...) -> Any:",
            "    \"\"\"Get a variable value with optional default.\"\"\"",
            "    ...",
            "",
            "def put(key: str, value: Any, ttl: Optional[timedelta] = ...) -> None:",
            "    \"\"\"Store a variable with optional TTL.\"\"\"",
            "    ...",
            "",
            "def delete(key: str) -> None:",
            "    \"\"\"Delete a variable.\"\"\"",
            "    ...",
            "",
            "def show_all() -> dict[str, dict[str, Any]]:",
            "    \"\"\"Get all stored variables with metadata.\"\"\"",
            "    ...",
            "",
            "# Module-level attributes for LSP compatibility",
            "__all__: list[str]",
        ])
        
        # Add __all__ list for better LSP support
        if variables:
            var_names = [name for name in sorted(variables.keys()) if name.isidentifier()]
            all_exports = var_names + ["refresh", "get", "put", "delete", "show_all"]
            lines.extend([
                "",
                "# Explicit exports for LSP autocompletion",
                f"__all__ = {all_exports!r}",
            ])
        
        return "\n".join(lines) + "\n"
    
    except Exception as e:
        return f"# Error generating stub file: {e}\n"


# For backwards compatibility and explicit access
get = store.get
put = store.put
delete = store.delete
show_all = store._get_all