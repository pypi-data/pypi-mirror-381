"""
Compatibility shim for old import paths.
This module redirects imports from the old scriptthing.core.analyzers to the new location.
"""

import warnings

# Issue deprecation warning
warnings.warn(
    "Importing from scriptthing.core.analyzers is deprecated. "
    "Use scriptthing.compiler.analyzers instead.",
    DeprecationWarning,
    stacklevel=2
)

# Import everything from the new location
from ..compiler.analyzers import *
from ..compiler.analyzers import (
    AnalysisContext,
    analyze_script,
    save_metadata,
    run_custom_pipeline,
    ANALYZER_PIPELINE,
    analyze_language,
    analyze_argparse,
    analyze_output_format,
    analyze_declarative_cli
)