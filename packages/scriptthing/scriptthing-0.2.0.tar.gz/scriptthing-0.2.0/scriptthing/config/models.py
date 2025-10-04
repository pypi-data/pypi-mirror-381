"""Pydantic models for ScriptThing configuration."""

from pathlib import Path
from typing import Literal, Optional
from pydantic import BaseModel, Field, field_validator, model_validator


class ParallelConfig(BaseModel):
    """Configuration for parallel execution features."""
    
    # Default to shell mode for stream command (enables piping and complex commands)
    # Set to false to require script name + template arguments by default
    default_shell_mode: bool = True
    
    # Default maximum number of concurrent workers
    # Set to 0 for auto-detection based on CPU cores
    default_max_workers: int = Field(default=0, ge=0)
    
    # Default timeout for parallel execution (in seconds)
    # Set to 0 for no timeout
    default_timeout: int = Field(default=0, ge=0)
    
    # Default strategy for parallel execution
    default_strategy: Literal["threads", "processes"] = "threads"
    
    # Default aggregation method for parallel results
    default_aggregation: Literal["all", "first", "last"] = "all"
    
    @field_validator('default_max_workers')
    @classmethod
    def validate_max_workers(cls, v: int) -> int:
        """Validate max workers is reasonable."""
        if v > 1000:
            raise ValueError("Max workers cannot exceed 1000 (unrealistic for most systems)")
        return v
    
    @field_validator('default_timeout')
    @classmethod
    def validate_timeout(cls, v: int) -> int:
        """Validate timeout is reasonable."""
        if v > 86400:  # 24 hours
            raise ValueError("Timeout cannot exceed 24 hours (86400 seconds)")
        return v


class ScriptThingConfig(BaseModel):
    """Main ScriptThing configuration model."""
    
    # Editor to use for opening files
    editor: str = "nvim"
    
    # Legacy global bin directory (no longer primary)
    bin: str = "~/.local/scriptthing/bin"
    
    # Default preference when both environment and scriptthing variables exist
    # Options: "env" (prefer environment variables) or "scriptthing" (prefer scriptthing variables)
    variable_preference: Literal["env", "scriptthing"] = "env"
    
    # Automatically generate IDE support files (.pyi stubs) when variables change
    # Set to false to disable automatic generation (use 'scriptthing vars generate-bindings' manually)
    auto_generate_bindings: bool = True
    
    # Enable single argument convenience for bash scripts
    # When true, scripts with exactly one variable parameter accept both positional and option syntax
    # e.g., both 'script "value"' and 'script --name "value"' work
    # Set to false to disable this convenience feature
    single_arg_convenience: bool = True
    
    # Parallel execution configuration
    parallel: ParallelConfig = Field(default_factory=ParallelConfig)
    
    @field_validator('editor')
    @classmethod
    def validate_editor(cls, v: str) -> str:
        """Validate editor is not empty."""
        if not v or not v.strip():
            raise ValueError("Editor cannot be empty")
        return v.strip()
    
    @field_validator('bin')
    @classmethod
    def validate_bin_path(cls, v: str) -> str:
        """Validate and expand bin path."""
        if not v or not v.strip():
            raise ValueError("Bin path cannot be empty")
        expanded_path = str(Path(v).expanduser())
        # Ensure the path is absolute
        if not Path(expanded_path).is_absolute():
            raise ValueError("Bin path must be absolute or use ~ for home directory")
        return expanded_path
    
    @model_validator(mode='after')
    def validate_config(self) -> 'ScriptThingConfig':
        """Post-validation to ensure configuration consistency."""
        # Additional validation logic can be added here
        return self
    
    def get_parallel_config(self) -> ParallelConfig:
        """Get parallel configuration with defaults applied."""
        return self.parallel
    
    def get_variable_preference(self) -> str:
        """Get variable preference setting."""
        return self.variable_preference
    
    def get_auto_generate_bindings(self) -> bool:
        """Get auto-generate bindings setting."""
        return self.auto_generate_bindings
    
    def get_single_arg_convenience(self) -> bool:
        """Get single argument convenience setting."""
        return self.single_arg_convenience
    
    def save_to_file(self, config_path: Optional[Path] = None) -> None:
        """Save configuration to TOML file."""
        import toml
        
        if config_path is None:
            from .config import get_config_path
            config_path = get_config_path()
        
        # Ensure parent directory exists
        config_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Convert to dict and structure for TOML
        config_dict = self.model_dump()
        
        # Create TOML structure
        toml_content = {
            "scriptthing": config_dict
        }
        
        # Write to file
        config_path.write_text(toml.dumps(toml_content))