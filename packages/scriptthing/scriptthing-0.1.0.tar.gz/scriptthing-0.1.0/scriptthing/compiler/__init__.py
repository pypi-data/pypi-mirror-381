"""
ScriptThing Compiler Module

Simplified decorator-based compilation pipeline including:
- Script compilation and transformation using decorators
- Language analysis and detection
- Context manager pipeline with setup/teardown
"""

from .core import compile_script
from .analyzers import analyze_script, AnalysisContext
from .context import CompilerContext
from .pipeline import run_pipeline, list_steps, get_step_info, compiler_step
# Import steps to register them
from . import steps

__all__ = [
    'compile_script',
    'run_pipeline',
    'compiler_step',
    'list_steps', 
    'get_step_info',
    'analyze_script',
    'AnalysisContext',
    'CompilerContext'
]