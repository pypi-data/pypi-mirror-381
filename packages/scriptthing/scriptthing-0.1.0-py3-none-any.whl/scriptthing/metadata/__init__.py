# Metadata utilities for defining MCP tool properties in scripts
from typing import List, Any, Optional 
from dataclasses import dataclass


@dataclass
class Parameter:
    """Represents a parameter for an MCP tool"""
    name: str
    description: str
    type: str = "string"
    required: bool = True
    enum: Optional[List[str]] = None
    default: Optional[Any] = None


@dataclass  
class MCPTool:
    """Represents MCP tool metadata"""
    name: str
    description: str
    parameters: List[Parameter]
    ai_instructions_before: Optional[str] = None
    ai_instructions_after: Optional[str] = None

    def __post_init__(self):
        # Sanitize the instructions 
        if self.ai_instructions_before:
            # literal new lines
            self.ai_instructions_before = self.ai_instructions_before.replace("\n", "\\n")
            # escape quotes
            self.ai_instructions_before = self.ai_instructions_before.replace("\"", '\\"')

        if self.ai_instructions_after:
            self.ai_instructions_after = self.ai_instructions_after.replace("\n", "\\n")
            self.ai_instructions_after = self.ai_instructions_after.replace("\"", '\\"')
    


__all__ = [
    "Parameter", 
    "MCPTool"
]
