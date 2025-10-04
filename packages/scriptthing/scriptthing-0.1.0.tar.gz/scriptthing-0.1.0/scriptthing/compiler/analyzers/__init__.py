"""ScriptThing analyzer system."""

from .context import AnalysisContext
from .manager import (
    analyze_script, 
    save_metadata, 
    run_custom_pipeline,
    ANALYZER_PIPELINE
)
from .language_analyzer import analyze_language
from .argparse_analyzer import analyze_argparse
from .output_format_analyzer import analyze_output_format
from .declarative_cli_analyzer import analyze_declarative_cli

__all__ = [
    'AnalysisContext',
    'analyze_script', 
    'save_metadata',
    'run_custom_pipeline',
    'ANALYZER_PIPELINE',
    'analyze_language',
    'analyze_argparse',
    'analyze_output_format',
    'analyze_declarative_cli'
]