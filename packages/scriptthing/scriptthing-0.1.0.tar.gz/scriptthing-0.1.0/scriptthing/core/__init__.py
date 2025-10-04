"""
Core scriptthing utilities for cross-language access

This module provides a unified interface to core scriptthing functionality
that can be accessed from scripts in any language through the bindings system.
"""

from ..utils import store
from ..config.config import (
    get_scriptthing_home,
    get_config_path, 
    get_or_create_config
)
from ..templating.paths import list_scripts, get_script_by_name, create_script_in_language
from ._execute_scripts import runscript
from ._script_metadata import ScriptMetadata, OutputType
from ..compiler import analyze_script, compile_script
from ..compiler.analyzers import save_metadata
from ..runtime import execute_script
from .parallel import stream

# Re-export core functionality
__all__ = [
    'store',
    'get_scriptthing_home',
    'get_config_path',
    'get_or_create_config', 
    'list_scripts',
    'get_script_by_name',
    'create_script_in_language',
    'runscript',
    'ScriptMetadata',
    'OutputType',
    'analyze_script',
    'save_metadata',
    'execute_script',
    'compile_script',
    # Simplified parallel execution
    'stream'
]
