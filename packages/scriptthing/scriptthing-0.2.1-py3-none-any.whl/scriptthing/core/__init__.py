"""
Core scriptthing utilities for script management

This module provides a unified interface to core scriptthing functionality
for managing scripts, functions, and extensions.
"""

from ..utils import store
from ..config.config import (
    get_scriptthing_home,
    get_config_path, 
    get_or_create_config
)
from ..templating.paths import list_scripts, get_script_by_name, create_script_in_language
from ._script_metadata import ScriptMetadata, OutputType

# Re-export core functionality
__all__ = [
    'store',
    'get_scriptthing_home',
    'get_config_path',
    'get_or_create_config', 
    'list_scripts',
    'get_script_by_name',
    'create_script_in_language',
    'ScriptMetadata',
    'OutputType'
]
