from pathlib import Path

from .analyzers import AnalysisContext
from .pipeline import run_pipeline
# Import steps to register them
from . import steps


def compile_script(script_path: Path) -> tuple[str, AnalysisContext]:
    """
    Compilation step: modify script content before execution.
    
    Uses the simplified decorator-based pipeline approach.
    
    Args:
        script_path: Path to the original script
        
    Returns:
        Tuple of (compiled_content, analysis_context)
        compiled_content is the transformed script content as a string
        analysis_context contains the full script analysis with metadata and methods
    """
    return run_pipeline(script_path)
