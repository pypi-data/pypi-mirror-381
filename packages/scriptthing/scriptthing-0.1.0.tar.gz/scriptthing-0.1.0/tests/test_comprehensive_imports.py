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
    from scriptthing.cli import generate_commands
    
    # Core modules
    from scriptthing import core
    from scriptthing.core import _execute_scripts
    from scriptthing.core import _script_metadata
    
    # Compiler modules (new)
    from scriptthing.compiler import analyzers
    from scriptthing.compiler.analyzers import context
    from scriptthing.compiler.analyzers import manager
    from scriptthing.compiler.analyzers import language_analyzer
    from scriptthing.compiler.analyzers import argparse_analyzer
    from scriptthing.compiler.analyzers import output_format_analyzer
    from scriptthing.compiler.analyzers import declarative_cli_analyzer
    from scriptthing.compiler import core as compiler_core
    
    # Runtime modules (new)
    from scriptthing.runtime import execution
    from scriptthing import runtime
    
    # Utils modules
    from scriptthing.utils import store
    from scriptthing.utils import cli as utils_cli
    
    # Config modules
    from scriptthing.config import config
    
    # Templating modules
    from scriptthing.templating import paths
    from scriptthing.templating import lang
    from scriptthing.templating import resources
    from scriptthing.templating import wrapping
    
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
    
    # Test runtime entry point
    from scriptthing.runtime import main
    assert main is not None

def test_critical_functions():
    """Test that critical functions are available"""
    
    # Test core analysis function
    from scriptthing.compiler.analyzers import analyze_script
    assert analyze_script is not None
    
    # Test script execution function
    from scriptthing.runtime import execute_script
    assert execute_script is not None
    
    # Test metadata classes are available
    from scriptthing.core import ScriptMetadata
    assert ScriptMetadata is not None