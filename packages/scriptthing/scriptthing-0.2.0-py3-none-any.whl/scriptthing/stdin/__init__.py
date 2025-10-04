"""
Standard input helpers for ScriptThing.

This module now dynamically replaces itself with an instance of a custom
`ModuleType` subclass so that it can take advantage of `functools.cached_property`.

The public API remains identical:

    import scriptthing.stdin as stdin

    data = stdin.read_json()     # ← legacy function API
    text = stdin.text            # ← new property API (computed once)

Any values derived from standard input are only read **once**, then cached for
subsequent calls.  This is particularly useful when a script needs to access
stdin in multiple formats (text, lines, json) without re-reading or seeking the
stream.
"""

from __future__ import annotations

import sys
import json as _json
from functools import cached_property
from types import ModuleType
from typing import Any, Dict, List


class _StdinModule(ModuleType):
    """Replacement module that lazily reads and caches *stdin* contents."""

    # ---------------------------------------------------------------------
    # Cached *raw* data ----------------------------------------------------
    # ---------------------------------------------------------------------
    @cached_property  # type: ignore[misc]
    def text(self) -> str:  # noqa: D401  (property, not method)
        """Return the full contents of *stdin*.

        The data is read at first access and subsequently cached on the module
        instance, ensuring the underlying *stdin* buffer is only consumed
        once.
        """

        return sys.stdin.read()

    # ------------------------------------------------------------------
    # Derived cached properties ----------------------------------------
    # ------------------------------------------------------------------
    @cached_property  # type: ignore[misc]
    def lines(self) -> List[str]:
        """Return *stdin* split into lines (without line-terminators)."""

        return [line.rstrip("\n\r") for line in self.text.splitlines()]

    @cached_property  # type: ignore[misc]
    def json(self) -> Dict[str, Any]:
        """Parse *stdin* as JSON and return the resulting object."""

        return _json.loads(self.text)

    @cached_property  # type: ignore[misc]
    def jsonl(self) -> List[Dict[str, Any]]:  # noqa: D401
        """Parse *stdin* as *JSON Lines* and return a list of objects."""

        return [_json.loads(line) for line in self.lines if line]

    # ------------------------------------------------------------------
    # Legacy function API ----------------------------------------------
    # ------------------------------------------------------------------
    # These are method definitions (note the *self* parameter) so that they
    # become bound to the module instance and can reference the cached
    # properties above.  This preserves the original functional API while
    # migrating the implementation to use cached data.

    def read_text(self) -> str:  # noqa: D401  (verb form maintained for BC)
        """Read all text from standard input (cached)."""

        return self.text

    def read_lines(self) -> List[str]:
        """Read all lines from standard input (cached)."""

        return self.lines

    def read_json(self) -> Dict[str, Any]:
        """Parse JSON from standard input (cached)."""

        return self.json

    def read_jsonl(self) -> List[Dict[str, Any]]:  # noqa: D401
        """Parse JSON Lines (JSONL) from standard input (cached)."""

        return self.jsonl

    # Aliases for convenience (legacy naming)
    read_string = read_text
    read_str = read_text

    # Alternative naming for JSONL
    read_lines_json = read_jsonl


# -------------------------------------------------------------------------
# Replace the original module object with an instance of the custom class.
# -------------------------------------------------------------------------

# _orig points to the automatically-created module when Python imported this
# file.  We reuse its namespace so that any symbols defined above (including
# the class itself) remain available on the resulting replacement module.

_orig = sys.modules[__name__]
_replacement = _StdinModule(__name__)
_replacement.__dict__.update(_orig.__dict__)

# Swap *sys.modules* entry in-place so that *import scriptthing.stdin* yields
# the new module instance everywhere.
sys.modules[__name__] = _replacement

# Help static type checkers (mypy, pyright, etc.) recognise the augmented API.
# Consumers importing this module will see the attributes listed in *__all__.

__all__ = [
    # Properties / cached variants
    "text",
    "lines",
    "json",
    "jsonl",
    # Functions (legacy API)
    "read_text",
    "read_lines",
    "read_json",
    "read_jsonl",
    "read_string",
    "read_str",
]

