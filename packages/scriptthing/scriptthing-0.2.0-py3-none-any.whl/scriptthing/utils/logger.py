from __future__ import annotations

"""Lightweight logging utilities for scripthing scripts.

Usage:
    from scriptthing.utils import log  # global ready-to-use logger

    log.info("Something happened")

Metadata comments in the script can control the same options:

    # log-level: DEBUG  # DEBUG | INFO | WARNING | ERROR | CRITICAL
    # log-color: no     # yes/true/1 | no/false/0 | auto (default)

Env vars take precedence over comments:

    SCRIPTTHING_LOG_LEVEL, SCRIPTTHING_LOG_COLOR
"""

import logging
import os
import json as _json
from typing import Optional, Union, Any, Dict
from pathlib import Path

__all__ = [
    "set_level",
    "log",
    "debug",
    "info",
    "warning",
    "error",
    "critical",
]

_DEFAULT_LEVEL = logging.INFO
_ENV_VAR = "SCRIPTTHING_LOG_LEVEL"

# ---------------------------------------------------------------------------
# Pull logging-related metadata from the standard analysis object. No
# additional fallbacks are performed – the consuming application must ensure
# that the analyzer pipeline has populated these values.
# ---------------------------------------------------------------------------


# Detect color preference (default determined later)
try:
    import scriptthing as _st_mod  # pylint: disable=import-error
    _SCRIPT_METADATA = (
        (_st_mod.analysis.get('logging', {}) if _st_mod.analysis else {})  # type: ignore[attr-defined]
        or {}
    )
except Exception:  # pragma: no cover
    _SCRIPT_METADATA = {}

# ---------------------------------------------------------------------------

_LOGGING_KWARGS = {"exc_info", "stack_info", "stacklevel", "extra"}


def _initial_level() -> int:
    """Determine the initial log level.

    Priority order:
    1. The *SCRIPTTHING_LOG_LEVEL* env var (e.g. ``DEBUG``/``INFO``/``WARNING``)
    2. Fallback to :data:`_DEFAULT_LEVEL`.
    """
    env_val = os.getenv(_ENV_VAR, "")
    if env_val:
        return getattr(logging, env_val.upper(), _DEFAULT_LEVEL)

    meta_level = _SCRIPT_METADATA.get("level")
    if meta_level:
        return getattr(logging, meta_level.upper(), _DEFAULT_LEVEL)

    return _DEFAULT_LEVEL


def _determine_color_setting() -> str:
    """Return final color setting string after evaluating env and metadata."""
    env_val = os.getenv("SCRIPTTHING_LOG_COLOR")
    if env_val is not None:
        return env_val.lower()

    meta_color = _SCRIPT_METADATA.get("color")
    if meta_color is not None:
        return meta_color.lower()

    return "auto"


def _configure_root(level: int) -> None:
    """Configure the root logger (run once)."""
    root = logging.getLogger()
    if root.handlers:  # Already configured by the application/user.
        return

    # Build handler with optional ANSI colors
    handler = logging.StreamHandler()

    use_color_config = _determine_color_setting()

    class _ColorFormatter(logging.Formatter):
        _RESET = "\033[0m"
        _COLORS = {
            logging.DEBUG: "\033[38;5;244m",  # grey
            logging.INFO: "\033[32m",         # green
            logging.WARNING: "\033[33m",      # yellow
            logging.ERROR: "\033[31m",        # red
            logging.CRITICAL: "\033[1;31m",   # bold red
        }

        def format(self, record: logging.LogRecord) -> str:  # type: ignore[override]
            colorize = (
                use_color_config in {"1", "yes", "true"}
                or (use_color_config == "auto" and handler.stream.isatty())
            )

            if colorize:
                color = self._COLORS.get(record.levelno, "")
                reset = self._RESET if color else ""
                record.level_initial_colored = f"{color}{record.levelname[0]}{reset}"
                record.name_colored = f"{color}{record.name}{reset}"
            else:
                record.level_initial_colored = record.levelname[0]
                record.name_colored = record.name

            return super().format(record)

    formatter = _ColorFormatter(
        fmt="%(asctime)s [%(level_initial_colored)s] %(name_colored)s: %(message)s",
        datefmt="%H:%M:%S",
    )

    handler.setFormatter(formatter)
    root.setLevel(level)
    root.addHandler(handler)

    # Avoid duplicate logging when this module is re-imported in interactive environments
    root.propagate = False


# Perform one-time root logger setup when the module is imported.
_configure_root(_initial_level())


# ---------------------------------------------------------------------------
# Logger resolution - uses a default logger name since script metadata 
# is no longer available through the legacy analysis system.
# ---------------------------------------------------------------------------

_LOGGER_CACHE: Optional[logging.Logger] = None


def _get_logger_instance() -> logging.Logger:
    """Return the singleton logger using a default name."""
    global _LOGGER_CACHE  # noqa: PLW0603
    if _LOGGER_CACHE is not None:
        return _LOGGER_CACHE

    # Use a default logger name since we no longer have script metadata
    # available through the legacy analysis system
    logger_name = "scriptthing"
    _LOGGER_CACHE = logging.getLogger(logger_name)
    return _LOGGER_CACHE


# Proxy object so `from scriptthing.utils import log` works before logger
# resolution. Attribute access is forwarded to the real logger.


class _LoggerProxy:
    def __getattr__(self, attr: str):  # noqa: D401
        return getattr(_get_logger_instance(), attr)

    def __setattr__(self, attr: str, value):  # noqa: D401
        return setattr(_get_logger_instance(), attr, value)


# Exported proxy
log = _LoggerProxy()  # type: ignore[assignment]

# Internal helper kept for tests/advanced usage
def _get_logger(name: Optional[str] = None) -> logging.Logger:  # noqa: D401
    if name is None:
        return _get_logger_instance()
    return logging.getLogger(name)


def _split_kwargs(kwargs: Dict[str, Any]) -> tuple[Dict[str, Any], Dict[str, Any]]:
    """Separate standard logging kwargs from structured-data kwargs."""
    log_kwargs: Dict[str, Any] = {}
    data_kwargs: Dict[str, Any] = {}
    for k, v in kwargs.items():
        if k in _LOGGING_KWARGS:
            log_kwargs[k] = v
        else:
            data_kwargs[k] = v
    return log_kwargs, data_kwargs


def _prepare_message(msg: Any, data_kwargs: Dict[str, Any]) -> str:
    """Convert *msg* and extra key/value pairs into a JSON string.

    Rules:
    1. Always emit valid JSON.
    2. Message-only strings are wrapped as `{"message": "..."}`.
    3. Lists/tuples become `{"data": [... ]}` unless they are already inside
       a dict.
    4. `data_kwargs` are merged into the resulting object (override duplicates).
    """

    # Determine base payload
    if isinstance(msg, dict):
        payload: Any = {**msg}  # shallow copy to avoid mutating caller data
    elif isinstance(msg, (list, tuple)):
        payload = {"data": list(msg)}  # convert tuple to list for JSON
    elif msg is None:
        payload = {}
    else:
        payload = {"message": str(msg)}

    # Merge in structured kwargs (if both dict)
    if data_kwargs:
        if isinstance(payload, dict):
            payload.update(data_kwargs)
        else:
            # If payload is non-dict (shouldn't happen after conditions), wrap
            payload = {"data": payload, **data_kwargs}

    return _json.dumps(payload, separators=(",", ":"), sort_keys=True, ensure_ascii=False, default=str)


def set_level(level: Union[int, str]) -> None:
    """Dynamically set the log level for the root logger.

    Args:
        level: Either a numeric log level (e.g. :data:`logging.DEBUG`) or a
            level name string (``"debug"`` / ``"INFO"`` / ...).
    """
    if isinstance(level, str):
        level = getattr(logging, level.upper(), _DEFAULT_LEVEL)
    logging.getLogger().setLevel(level)  # type: ignore[arg-type]


# ---------------------------------------------------------------------------
# Convenience wrappers exposed at module level (avoids importing the logger)
# ---------------------------------------------------------------------------

def _format_message(msg: Any) -> str:
    """Convert *msg* to a loggable string.

    If *msg* is a mapping, encode it as a compact JSON string to enable
    structured logging that downstream processors can parse.
    """
    # For mappings, sequences, or other JSON-serialisable objects, emit compact JSON.
    if isinstance(msg, (dict, list, tuple)):
        return _json.dumps(
            msg,
            separators=(",", ":"),
            sort_keys=isinstance(msg, dict),
            ensure_ascii=False,
            default=str,
        )

    # Fallback to JSON encoding for numeric/boolean types to avoid quoting
    if isinstance(msg, (int, float, bool, type(None))):
        return _json.dumps(msg, ensure_ascii=False)

    # Last resort – just str()
    return str(msg)


def debug(msg: Any = None, *args, **kwargs):
    """Log *msg* with DEBUG level using the global logger.

    Accepts either a string or a mapping (will be JSON‐encoded).
    """
    log_kwargs, data_kwargs = _split_kwargs(kwargs)
    log.debug(_prepare_message(msg, data_kwargs), *args, **log_kwargs)


def info(msg: Any = None, *args, **kwargs):
    """Log *msg* with INFO level using the global logger."""
    log_kwargs, data_kwargs = _split_kwargs(kwargs)
    log.info(_prepare_message(msg, data_kwargs), *args, **log_kwargs)


def warning(msg: Any = None, *args, **kwargs):
    """Log *msg* with WARNING level using the global logger."""
    log_kwargs, data_kwargs = _split_kwargs(kwargs)
    log.warning(_prepare_message(msg, data_kwargs), *args, **log_kwargs)


def error(msg: Any = None, *args, **kwargs):
    """Log *msg* with ERROR level using the global logger."""
    log_kwargs, data_kwargs = _split_kwargs(kwargs)
    log.error(_prepare_message(msg, data_kwargs), *args, **log_kwargs)


def critical(msg: Any = None, *args, **kwargs):
    """Log *msg* with CRITICAL level using the global logger."""
    log_kwargs, data_kwargs = _split_kwargs(kwargs)
    log.critical(_prepare_message(msg, data_kwargs), *args, **log_kwargs)