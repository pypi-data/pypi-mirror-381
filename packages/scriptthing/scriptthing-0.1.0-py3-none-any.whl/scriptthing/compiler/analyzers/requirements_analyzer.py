import ast
import re
from .context import AnalysisContext


REQ_TAG_RE = re.compile(r"^\s*#\s*requires:\s*(?P<req>.+)$", re.IGNORECASE)


def analyze_requirements(context: AnalysisContext) -> None:
    """Extract script requirements into context.metadata['requirements'].

    Sources:
    - Explicit lines: '# requires: <pip-requirement>' (can appear multiple times)
    - Implicit: Python imports (collect top-level names) -> provided as 'imports' for later mapping

    We do not map imports to PyPI names here; executor may choose to install explicit ones only
    or attempt a best-effort mapping.
    """
    content = context.content
    if not content:
        return

    explicit: list[str] = []
    for line in content.splitlines():
        m = REQ_TAG_RE.match(line)
        if m:
            req = m.group('req').strip()
            if req:
                explicit.append(req)

    requirements = {
        'explicit': explicit,
        'imports': [],
    }

    # Only parse imports for python scripts
    if context.get('lang') == 'python':
        try:
            tree = ast.parse(content)
            names: set[str] = set()
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        base = alias.name.split('.')[0]
                        names.add(base)
                elif isinstance(node, ast.ImportFrom):
                    if node.module:
                        base = node.module.split('.')[0]
                        names.add(base)
            requirements['imports'] = sorted(names)
        except Exception:
            pass

    context.set('requirements', requirements)

