from pathlib import Path
from typing import Literal
from pydantic import BaseModel, Field, field_validator, ConfigDict

OutputType = Literal["json", "text"]


class ScriptMetadata(BaseModel):
    """Metadata for a script including path and output configuration."""
    
    model_config = ConfigDict(
        # Allow positional arguments for backward compatibility
        arbitrary_types_allowed=True,
        # Enable validation on assignment
        validate_assignment=True,
        # Enable extra fields to be ignored
        extra='forbid'
    )
    
    script_path: Path = Field(..., description="Path to the script file")
    output_type: OutputType = Field(default="text", description="Expected output format")
    
    def __init__(self, script_path: Path, output_type: OutputType = "text", **kwargs):
        """Initialize ScriptMetadata with positional arguments for backward compatibility."""
        super().__init__(script_path=script_path, output_type=output_type, **kwargs)
    
    @field_validator('script_path')
    @classmethod
    def validate_script_path(cls, v: Path) -> Path:
        """Validate that the script path exists and is a file."""
        if not v.exists():
            raise ValueError(f"Script path does not exist: {v}")
        if not v.is_file():
            raise ValueError(f"Script path is not a file: {v}")
        return v
    
    @field_validator('output_type')
    @classmethod
    def validate_output_type(cls, v: str) -> str:
        """Validate output type is one of the allowed values."""
        allowed_types = ["json", "text"]
        if v not in allowed_types:
            raise ValueError(f"Output type must be one of {allowed_types}, got: {v}")
        return v
    
    def model_post_init(self, __context) -> None:
        """Post-initialization validation."""
        # Ensure script_path is resolved to absolute path
        if not self.script_path.is_absolute():
            self.script_path = self.script_path.resolve()
    
    def to_dict(self) -> dict:
        """Convert to dictionary for serialization."""
        return self.model_dump()
    
    @classmethod
    def from_dict(cls, data: dict) -> 'ScriptMetadata':
        """Create instance from dictionary."""
        return cls(**data)
