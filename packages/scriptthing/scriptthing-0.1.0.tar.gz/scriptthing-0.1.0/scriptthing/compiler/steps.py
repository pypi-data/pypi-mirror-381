"""Simplified compiler steps using decorator pattern.

Example:
    @compiler_step()  # Uses auto-incrementing default order
    def my_step(context):
        # Setup
        context.set_compiler_metadata('started', True)
        
        # Transform content
        modified = context.content + "\\n# Modified by my_step"
        context.update_content(modified)
        
        yield  # Main processing point
        
        # Teardown
        context.set_compiler_metadata('completed', True)
        
    @compiler_step(order=5)  # Explicit order for priority
    def priority_step(context):
        yield
"""
import re
from typing import Generator, Optional

from .pipeline import compiler_step
from .context import CompilerContext




@compiler_step()
def addargname(context: CompilerContext) -> Generator[None, None, None]:
    """Add argument names to arg() calls in Python scripts."""
    # Setup
    detected_lang: Optional[str] = context.get('lang')
    context.set_compiler_metadata('addargname_started', True)
    
    # Only process Python files
    if detected_lang != 'python':
        context.set_compiler_metadata('addargname_skipped', True)
        yield
        return
    
    # Transform arg() calls
    pattern: re.Pattern[str] = re.compile(r"^(\s*)(\w+)\s*=\s*arg\((.*?)\)\s*$")
    output_lines: list[str] = []
    transformed_calls: int = 0
    
    for line in context.content.splitlines():
        match = pattern.match(line)
        if match:
            whitespace: str
            name: str
            args: str
            whitespace, name, args = match.groups()
            new_line: str = f"{whitespace}{name} = arg(\"{name}\", {args})"
            output_lines.append(new_line)
            transformed_calls += 1
        else:
            output_lines.append(line)
    
    context.update_content("\n".join(output_lines))
    context.set_compiler_metadata('transformed_calls', transformed_calls)
    
    yield  # Main processing
    
    # Teardown
    context.set_compiler_metadata('addargname_completed', True)


@compiler_step(order=20)
def environment_injection(context: CompilerContext) -> Generator[None, None, None]:
    """Inject environment-specific code based on analysis."""
    # Setup
    context.set_compiler_metadata('env_injection_started', True)
    
    # Get environment info from analysis
    env_info: dict = context.get('environment', {})
    
    # For now, just preserve content
    # In the future, could inject environment-specific imports, setup code, etc.
    
    yield  # Main processing point
    
    # Teardown
    context.set_compiler_metadata('env_injection_completed', True)


@compiler_step(order=30)
def imports_injection(context: CompilerContext) -> Generator[None, None, None]:
    """Inject additional imports based on analysis."""
    # Setup
    context.set_compiler_metadata('imports_injection_started', True)
    
    detected_lang: Optional[str] = context.get('lang', 'python')
    
    if detected_lang == 'python':
        content: str = context.content
        
        # Check if we need to inject scriptthing imports
        if 'scriptthing' not in content:
            # Could inject basic scriptthing imports here
            pass
    
    yield  # Main processing point
    
    # Teardown
    context.set_compiler_metadata('imports_injection_completed', True)


@compiler_step(order=40)
def output_formatting(context: CompilerContext) -> Generator[None, None, None]:
    """Add output formatting based on detected output type."""
    # Setup
    context.set_compiler_metadata('output_formatting_started', True)
    
    output_type: Optional[str] = context.get('output_format', {}).get('format')
    
    if output_type == 'json':
        # Could inject JSON formatting code here
        pass
    
    yield  # Main processing point
    
    # Teardown  
    context.set_compiler_metadata('output_formatting_completed', True)


@compiler_step(order=50)
def final_cleanup(context: CompilerContext) -> Generator[None, None, None]:
    """Final cleanup and validation of compiled content."""
    # Setup
    context.set_compiler_metadata('final_cleanup_started', True)
    
    # Clean up extra whitespace, validate syntax if needed
    content: str = context.content
    
    # Remove excessive blank lines
    cleaned_content: str = re.sub(r'\n\n\n+', '\n\n', content)
    context.update_content(cleaned_content)
    
    yield  # Main processing point
    
    # Teardown
    context.set_compiler_metadata('final_cleanup_completed', True)