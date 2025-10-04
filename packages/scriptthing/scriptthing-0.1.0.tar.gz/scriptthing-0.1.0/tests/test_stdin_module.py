"""Tests for :pymod:`scriptthing.stdin` replacement module."""
from __future__ import annotations

import importlib
import sys
from contextlib import contextmanager
from io import StringIO
from types import ModuleType
from typing import Any, Dict, Iterator

import pytest


# ---------------------------------------------------------------------------
# Helper utilities
# ---------------------------------------------------------------------------

@contextmanager
def _mock_stdin_context(buffer: str) -> Iterator[ModuleType]:
    """Context manager to import scriptthing.stdin with mocked stdin buffer."""
    # Save original stdin
    orig_stdin = sys.stdin
    
    # Remove previously imported module if present to force a clean import
    sys.modules.pop("scriptthing.stdin", None)
    
    try:
        # Set up mock stdin
        sys.stdin = StringIO(buffer)
        
        # Import the module with our mocked stdin
        mod = importlib.import_module("scriptthing.stdin")
        
        yield mod
        
    finally:
        # Always restore original stdin
        sys.stdin = orig_stdin


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


def test_text_and_lines_are_cached() -> None:
    with _mock_stdin_context("foo\nbar\n") as mod:
        # First access reads from the underlying StringIO
        assert mod.text == "foo\nbar\n"
        assert mod.lines == ["foo", "bar"]

        # Subsequent access should return the *same* object thanks to caching
        assert mod.text is mod.text  # identity check
        assert mod.lines is mod.lines


@pytest.mark.parametrize("payload, expected", [
    ("{\"x\": 1}", {"x": 1}),
    ("{\n\t\"hello\": \"world\"\n}", {"hello": "world"}),
])

def test_json_parsing(payload: str, expected: Dict[str, Any]) -> None:  # type: ignore[type-var]
    with _mock_stdin_context(payload) as mod:
        assert mod.json == expected
        # Legacy function name
        assert mod.read_json() == expected


def test_legacy_function_aliases() -> None:
    with _mock_stdin_context("abc") as mod:
        assert mod.read_text() == "abc"
        assert mod.read_string() == "abc"
        assert mod.read_str() == "abc"



def test_direct_import_jsonl() -> None:
    """`from scriptthing.stdin import jsonl` should yield parsed list."""

    with _mock_stdin_context('{"a":1}\n{"b":2}\n') as mod:
        assert mod.jsonl == [{"a": 1}, {"b": 2}]