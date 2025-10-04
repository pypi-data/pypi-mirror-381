"""
ScriptThing Runtime Module

This module contains all runtime and execution-related functionality including:
- Script execution and process management
- Language-specific execution handlers
- Runtime environment setup
"""

from .execution import execute_script, main

__all__ = [
    'execute_script',
    'main'
]