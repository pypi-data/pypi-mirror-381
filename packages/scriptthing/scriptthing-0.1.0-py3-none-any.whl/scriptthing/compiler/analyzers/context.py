"""Analysis context for script analyzer pipeline."""
from pathlib import Path
from typing import Dict, Any
from functools import cached_property


class AnalysisContext:
    """Context object passed through the analyzer pipeline.
    
    Provides access to script content and metadata, with methods for
    analyzers to update metadata directly instead of returning dicts.
    """
    
    def __init__(self, script_path: Path):
        """Initialize context with script path."""
        self.script_path = script_path
        self.metadata: Dict[str, Any] = {}
        # Make the absolute script path available to all analyzers
        self.metadata["script_path"] = str(script_path)
        
    @cached_property
    def content(self) -> str:
        """Load and cache script content."""
        try:
            with open(self.script_path, 'r') as f:
                return f.read()
        except (OSError, UnicodeDecodeError):
            return ""
    
    def set(self, key: str, value: Any) -> None:
        """Set a metadata value."""
        self.metadata[key] = value
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get a metadata value with optional default."""
        return self.metadata.get(key, default)
    
    def update(self, updates: Dict[str, Any]) -> None:
        """Update metadata with a dictionary of values."""
        self.metadata.update(updates)
    
    def has(self, key: str) -> bool:
        """Check if a metadata key exists."""
        return key in self.metadata
    
    def set_nested(self, path: str, value: Any) -> None:
        """Set a nested metadata value using dot notation (e.g., 'argparse.has_parser')."""
        keys = path.split('.')
        current = self.metadata
        
        # Navigate to the parent dictionary
        for key in keys[:-1]:
            if key not in current:
                current[key] = {}
            current = current[key]
        
        # Set the final value
        current[keys[-1]] = value
    
    def get_nested(self, path: str, default: Any = None) -> Any:
        """Get a nested metadata value using dot notation."""
        keys = path.split('.')
        current = self.metadata
        
        try:
            for key in keys:
                current = current[key]
            return current
        except (KeyError, TypeError):
            return default
    
    def to_dict(self) -> Dict[str, Any]:
        """Return the metadata as a dictionary."""
        return self.metadata.copy()