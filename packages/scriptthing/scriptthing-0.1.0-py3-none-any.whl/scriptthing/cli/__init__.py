"""
scriptthing CLI module

This module provides the command-line interface for scriptthing.
All commands are organized into separate modules for better maintainability.
"""

from .base import cli
from .script_commands import register_script_commands
from .generate_commands import register_generate_commands
from .vars_commands import register_vars_commands
from .parallel_commands import register_parallel_commands
from .modules_commands import register_modules_commands
from .repo_commands import register_repo_commands

# Register all command modules with the main CLI
register_script_commands(cli)
register_generate_commands(cli)
register_vars_commands(cli)
register_parallel_commands(cli)
register_modules_commands(cli)
register_repo_commands(cli)

# Ensure internal repo is registered
try:
    from ..repo import install_internal_repo_if_needed
    install_internal_repo_if_needed()
except Exception:
    pass

# Export the main CLI entry point
__all__ = ['cli']
