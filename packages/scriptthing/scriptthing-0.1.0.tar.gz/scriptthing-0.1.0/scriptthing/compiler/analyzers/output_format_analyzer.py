"""Output format analyzer for scripts."""
import re
from .context import AnalysisContext


def analyze_output_format(context: AnalysisContext) -> None:
    """Parse output format from script comments and update context metadata."""
    content = context.content
    
    if not content:
        return
    
    for line in content.split('\n'):
        line = line.strip()
        if line.startswith('#') and 'output:' in line:
            match = re.search(r'output:\s*(\w+)', line)
            if match:
                context.set_nested('output_format.format', match.group(1))
                return