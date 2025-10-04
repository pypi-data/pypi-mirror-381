"""Declarative CLI analyzer for scripts."""
import re
from .context import AnalysisContext


# Pattern to match declarative CLI function calls
_DECLARATIVE_CLI_FUNCTIONS = ['program', 'arg', 'command']
_PATTERN = re.compile("|".join([
    f"^.*{fn}\\(.*\\).*$"
    for fn in _DECLARATIVE_CLI_FUNCTIONS
]))


def analyze_declarative_cli(context: AnalysisContext) -> None:
    """Analyze script for declarative CLI patterns and update context metadata."""
    content = context.content
    
    if not content:
        context.set_nested('declarative_cli.has_declarative_cli', False)
        return
    
    try:
        potential_matches = [_PATTERN.match(line) for line in content.splitlines()]
        matches = [match.group(0) for match in potential_matches if match is not None]
        
        if matches:
            context.set_nested('declarative_cli.has_declarative_cli', True)
            context.set_nested('declarative_cli.code', '\n'.join(matches))
        else:
            context.set_nested('declarative_cli.has_declarative_cli', False)
            
    except Exception:
        context.set_nested('declarative_cli.has_declarative_cli', False)


