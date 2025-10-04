"""
Comprehensive import test for all scriptthing modules
"""
import pytest

def test_all_scriptthing_imports():
    """Test that all scriptthing modules can be imported without errors"""
    
    # Main package
    import scriptthing
    
    # CLI modules
    from scriptthing.cli import cli
    from scriptthing.cli import base
    from scriptthing.cli import script_commands
    from scriptthing.cli import vars_commands
    # generate_commands removed in simplification
    
    # Core modules
    from scriptthing import core
    # _execute_scripts removed as part of runtime simplification
    from scriptthing.core import _script_metadata
    
    # Compiler and runtime modules removed for public release simplification
    
    # Utils modules
    from scriptthing.utils import store
    from scriptthing.utils import cli as utils_cli
    
    # Config modules
    from scriptthing.config import config
    
    # Templating modules
    from scriptthing.templating import paths
    from scriptthing.templating import lang
    from scriptthing.templating import resources
    
    # Shell modules
    from scriptthing import shell
    
    # Stdin helpers (replaces former testing module)
    from scriptthing import stdin
    
    # Metadata modules
    from scriptthing import metadata
    
    # All imports successful
    assert True

def test_entry_points():
    """Test that entry points work correctly"""
    
    # Test CLI entry point
    from scriptthing.cli import cli
    assert cli is not None
    
    # Runtime entry point removed

def test_critical_functions():
    """Test that critical functions are available"""
    
    # Analysis and execution functions removed in simplification
    
    # Test metadata classes are available
    from scriptthing.core import ScriptMetadata
    assert ScriptMetadata is not None