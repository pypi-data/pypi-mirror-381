import yaml
from pathlib import Path
from typing import Dict, Any, List, Callable
from .context import AnalysisContext
from .language_analyzer import analyze_language
from .requirements_analyzer import analyze_requirements
from .argparse_analyzer import analyze_argparse
from .output_format_analyzer import analyze_output_format
from .declarative_cli_analyzer import analyze_declarative_cli
from .logging_analyzer import analyze_logging_settings
from ..bash_magic import analyze_bash_magic


# Define the analyzer pipeline - functions that take AnalysisContext and return None
ANALYZER_PIPELINE: List[Callable[[AnalysisContext], None]] = [
    analyze_language,
    analyze_output_format,
    analyze_declarative_cli,
    analyze_logging_settings,
    analyze_requirements,
]


def analyze_script(script_path: Path) -> AnalysisContext:
    """Analyze a script using the pipeline approach and return the context object."""
    context = AnalysisContext(script_path)
    
    # Run the core pipeline
    for analyzer in ANALYZER_PIPELINE:
        analyzer(context)
    
    # Run language-specific analyzers based on detected language
    detected_lang = context.get('lang')
    if detected_lang == 'python':
        analyze_argparse(context)
    elif detected_lang == 'shell':
        analyze_bash_magic(context)
    
    return context


def run_custom_pipeline(script_path: Path, analyzers: List[Callable[[AnalysisContext], None]]) -> AnalysisContext:
    """Run a custom analyzer pipeline on a script.
    
    Args:
        script_path: Path to the script to analyze
        analyzers: List of analyzer functions that take AnalysisContext and return None
        
    Returns:
        AnalysisContext with accumulated metadata
    """
    context = AnalysisContext(script_path)
    
    for analyzer in analyzers:
        analyzer(context)
    
    return context





def save_metadata(script_path: Path, metadata: Dict[str, Any]) -> Path:
    """Save metadata to a YAML file."""
    metadata_path = script_path.with_suffix('.meta.yaml')
    
    with open(metadata_path, 'w') as f:
        yaml.dump(metadata, f, default_flow_style=False, sort_keys=False)
    
    return metadata_path