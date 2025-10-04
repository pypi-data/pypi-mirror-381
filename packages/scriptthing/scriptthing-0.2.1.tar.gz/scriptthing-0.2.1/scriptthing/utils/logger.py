from __future__ import annotations

"""Lightweight logging utilities for scriptthing scripts.

Usage:
    from scriptthing.utils import log  # global ready-to-use logger

    log.info("Something happened")

Environment variables:
    SCRIPTTHING_LOG_LEVEL: DEBUG | INFO | WARNING | ERROR | CRITICAL
    SCRIPTTHING_LOG_COLOR: yes/true/1 | no/false/0 | auto (default)
"""

import logging
import os
import sys
from typing import Optional, Union

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


def _get_log_level() -> int:
    """Get log level from environment or use default."""
    env_val = os.getenv("SCRIPTTHING_LOG_LEVEL", "")
    if env_val:
        return getattr(logging, env_val.upper(), _DEFAULT_LEVEL)
    return _DEFAULT_LEVEL


def _should_use_colors() -> bool:
    """Determine if colors should be used based on environment."""
    env_val = os.getenv("SCRIPTTHING_LOG_COLOR", "auto")
    if env_val.lower() in {"1", "yes", "true"}:
        return True
    elif env_val.lower() in {"0", "no", "false"}:
        return False
    # auto: use colors if stdout is a terminal
    return hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()


def _setup_logger() -> logging.Logger:
    """Set up and return the scriptthing logger."""
    logger = logging.getLogger("scriptthing")
    
    # Don't reconfigure if already set up
    if logger.handlers:
        return logger
    
    handler = logging.StreamHandler()
    use_colors = _should_use_colors()
    
    if use_colors:
        class ColorFormatter(logging.Formatter):
            COLORS = {
                logging.DEBUG: "\033[38;5;244m",    # grey
                logging.INFO: "\033[32m",           # green  
                logging.WARNING: "\033[33m",        # yellow
                logging.ERROR: "\033[31m",          # red
                logging.CRITICAL: "\033[1;31m",     # bold red
            }
            RESET = "\033[0m"
            
            def format(self, record):
                color = self.COLORS.get(record.levelno, "")
                record.levelname = f"{color}{record.levelname}{self.RESET}" if color else record.levelname
                return super().format(record)
        
        formatter = ColorFormatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s", "%H:%M:%S")
    else:
        formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s", "%H:%M:%S")
    
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(_get_log_level())
    logger.propagate = False
    
    return logger


# Set up the logger
_logger = _setup_logger()


class _LoggerProxy:
    """Proxy object so imports work before logger initialization."""
    def __getattr__(self, attr: str):
        return getattr(_logger, attr)

    def __setattr__(self, attr: str, value):
        return setattr(_logger, attr, value)


# Exported logger proxy
log = _LoggerProxy()


def set_level(level: Union[int, str]) -> None:
    """Set the log level dynamically.
    
    Args:
        level: Either a numeric log level or level name string.
    """
    if isinstance(level, str):
        level = getattr(logging, level.upper(), _DEFAULT_LEVEL)
    _logger.setLevel(level)


# Convenience functions
def debug(msg, *args, **kwargs):
    """Log message with DEBUG level."""
    _logger.debug(str(msg), *args, **kwargs)


def info(msg, *args, **kwargs):
    """Log message with INFO level.""" 
    _logger.info(str(msg), *args, **kwargs)


def warning(msg, *args, **kwargs):
    """Log message with WARNING level."""
    _logger.warning(str(msg), *args, **kwargs)


def error(msg, *args, **kwargs):
    """Log message with ERROR level."""
    _logger.error(str(msg), *args, **kwargs)


def critical(msg, *args, **kwargs):
    """Log message with CRITICAL level."""
    _logger.critical(str(msg), *args, **kwargs)