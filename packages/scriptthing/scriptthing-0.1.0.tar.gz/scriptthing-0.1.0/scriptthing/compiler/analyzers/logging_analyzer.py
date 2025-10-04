from __future__ import annotations

"""Logging settings analyzer.

Parses ``# log-level: <LEVEL>`` and ``# log-color: <VALUE>`` comments so that
other components (e.g. the logger) can respect script-local preferences.
"""

import re
from .context import AnalysisContext


_LEVEL_PATTERN = re.compile(r"log-level:\s*([a-zA-Z]+)", re.IGNORECASE)
_COLOR_PATTERN = re.compile(r"log-color:\s*([a-zA-Z0-9]+)", re.IGNORECASE)


def analyze_logging_settings(context: AnalysisContext) -> None:
    """Extract logging settings from script comments into metadata."""
    content = context.content
    if not content:
        return

    level: str | None = None
    color: str | None = None

    for line in content.splitlines():
        stripped = line.strip()
        if not stripped.startswith('#'):
            continue

        if (m := _LEVEL_PATTERN.search(stripped)) and level is None:
            level = m.group(1).upper()
        elif (m := _COLOR_PATTERN.search(stripped)) and color is None:
            color = m.group(1).lower()

        if level and color:
            break

    if level:
        context.set_nested('logging.level', level)
    if color:
        context.set_nested('logging.color', color)