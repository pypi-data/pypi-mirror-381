"""Compiler context for script compilation pipeline."""
from pathlib import Path
from typing import Dict, Any

from .analyzers import AnalysisContext


class CompilerContext:
    """Context object passed through the compiler pipeline.
    
    Contains the script content being compiled and provides access to
    all analysis metadata. Compiler steps operate on the content through
    this context object.
    """
    
    def __init__(self, script_path: Path, analysis_context: AnalysisContext):
        """Initialize compiler context with script path and analysis results."""
        self.script_path = script_path
        self.analysis_context = analysis_context
        
        # Start with original content - will be modified by compiler steps
        self.content = analysis_context.content
        
        # Compiler-specific metadata (separate from analysis metadata)
        self.compiler_metadata: Dict[str, Any] = {}
        
    @property
    def metadata(self) -> Dict[str, Any]:
        """Access to analysis metadata (read-only for compiler steps)."""
        return self.analysis_context.metadata
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get an analysis metadata value with optional default."""
        return self.analysis_context.get(key, default)
    
    def get_nested(self, path: str, default: Any = None) -> Any:
        """Get a nested analysis metadata value using dot notation."""
        return self.analysis_context.get_nested(path, default)
    
    def has(self, key: str) -> bool:
        """Check if an analysis metadata key exists."""
        return self.analysis_context.has(key)
    
    def set_compiler_metadata(self, key: str, value: Any) -> None:
        """Set a compiler-specific metadata value."""
        self.compiler_metadata[key] = value
    
    def get_compiler_metadata(self, key: str, default: Any = None) -> Any:
        """Get a compiler-specific metadata value with optional default."""
        return self.compiler_metadata.get(key, default)
    
    def update_content(self, new_content: str) -> None:
        """Update the compiled script content."""
        self.content = new_content
    
    def get_lines(self) -> list[str]:
        """Get script content as list of lines."""
        return self.content.split('\n')
    
    def set_lines(self, lines: list[str]) -> None:
        """Set script content from list of lines."""
        self.content = '\n'.join(lines)
    
    def to_dict(self) -> Dict[str, Any]:
        """Return both analysis and compiler metadata as a dictionary."""
        return {
            'analysis': self.analysis_context.to_dict(),
            'compiler': self.compiler_metadata.copy()
        }