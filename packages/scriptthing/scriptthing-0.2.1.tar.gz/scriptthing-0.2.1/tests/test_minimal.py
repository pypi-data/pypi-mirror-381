"""
Ultra-minimal test to isolate import issues
"""
from typing import Any


def test_minimal_import() -> None:
    """Test the absolute minimum import that should work"""
    # Only test the most basic import that should always work
    import scriptthing
    assert scriptthing is not None


def test_cli_import() -> None:
    """Test CLI import specifically"""
    from scriptthing.cli import cli
    assert cli is not None


