from __future__ import annotations

"""General date and time helpers used across ScriptThing.

This module is a central place for utilities that operate on *date* and
*time* related values so they can be reused by scripts, CLI helpers, and
internal code.

Currently it provides :func:`parse_duration`, which converts a
human-friendly time span expression (e.g. ``"2h 30m"`` or ``"45s"``) into
:class:`datetime.timedelta`.
"""

from datetime import timedelta

from humanfriendly import parse_timespan  # type: ignore

__all__ = ["parse_duration"]


def parse_duration(expr: str | None) -> timedelta | None:
    """Parse *expr* into :class:`datetime.timedelta`.

    The parsing is delegated to the excellent *humanfriendly* package so we
    get support for a wide range of expressions such as:

    * ``"10s"`` or ``"10 seconds"``
    * ``"5m"`` or ``"5 minutes"``
    * ``"2h 30m"``
    * ``"1 day"``

    If *expr* is ``None`` or an empty string, *None* is returned.  A
    :class:`ValueError` is raised for invalid input.
    """

    if not expr:
        return None

    seconds = parse_timespan(expr.strip(), default=None)
    if seconds is None:
        raise ValueError(f"Unable to parse duration string: {expr!r}")

    return timedelta(seconds=seconds)