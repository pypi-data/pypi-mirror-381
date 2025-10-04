from __future__ import annotations

"""Deprecated: use ``scriptthing.utils.dates`` instead.

This module remains for backwards-compatibility and simply re-exports
:func:`scriptthing.utils.dates.parse_duration`.
"""

from .dates import parse_duration  # noqa: F401

__all__ = ["parse_duration"]