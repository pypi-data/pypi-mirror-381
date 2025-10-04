#!/usr/bin/env python3

"""
Entry point for running scriptthing as a module.

This allows scriptthing to be invoked as:
    python -m scriptthing
"""

from .cli import cli

if __name__ == "__main__":
    cli()