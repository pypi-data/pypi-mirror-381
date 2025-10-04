#import tomllib as toml
try: 
    import tomllib as toml
except ImportError:
    import toml  # type: ignore

import shutil
from pathlib import Path
from typing import Dict, Any, Optional


def get_scriptthing_home() -> Path:
    return Path.home() / ".config/scriptthing"


def get_config_path() -> Path:
    config_path: Path = get_scriptthing_home()/"config.toml"
    return config_path


def get_or_create_config() -> Dict[str, Any]:
    config_path: Path = get_config_path()
    if not config_path.exists():
        # Try to find default config using multiple methods
        default_config_path: Optional[Path] = None
        
        # Method 1: Try relative path (development)
        dev_config_path: Path = Path(__file__).parent / "default_config.toml"
        if dev_config_path.exists():
            default_config_path = dev_config_path
        else:
            # Method 2: Try to find it in the package data
            try:
                from ..templating.resources import get_config_path as get_resource_config_path
                default_config_path = get_resource_config_path("default_config.toml")
            except (ImportError, FileNotFoundError):
                # Method 3: Create a minimal default config
                config_path.parent.mkdir(exist_ok=True, parents=True)
                default_content: str = '''[scriptthing]
editor = "vim"
bin = "~/.local/scriptthing/bin"
'''
                config_path.write_text(default_content)
                return toml.loads(default_content)["scriptthing"]
        
        if default_config_path:
            config_path.parent.mkdir(exist_ok=True, parents=True)
            shutil.copy(default_config_path, config_path)

    return toml.loads(config_path.read_text())["scriptthing"]


# Legacy bin helpers removed; repo bins are per-repo now


def get_or_create_functions_dir(config: Optional[Dict[str, Any]] = None) -> Path:
    """Get or create the directory for shell functions (only sourced in bash scripts)"""
    if config is None:
        config = get_or_create_config()
    functions_dir: Path = get_scriptthing_home() / "functions"
    functions_dir.mkdir(exist_ok=True, parents=True)
    return functions_dir


def get_or_create_extensions_dir(config: Optional[Dict[str, Any]] = None) -> Path:
    """Get or create the directory for shell extensions (always sourced in shell)"""
    if config is None:
        config = get_or_create_config()
    extensions_dir: Path = get_scriptthing_home() / "extensions"
    extensions_dir.mkdir(exist_ok=True, parents=True)
    return extensions_dir


def get_parallel_config(config: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Get parallel execution configuration with defaults"""
    if config is None:
        config = get_or_create_config()
    
    # Get parallel config section, with fallback defaults
    parallel_config = config.get("parallel", {})
    
    defaults = {
        "default_strategy": "threads",
        "default_max_workers": 0,
        "default_timeout": 0,
        "default_aggregation": "all"
    }
    
    # Merge with defaults
    for key, default_value in defaults.items():
        if key not in parallel_config:
            parallel_config[key] = default_value
    
    return parallel_config


def get_variable_preference(config: Optional[Dict[str, Any]] = None) -> str:
    """Get variable preference for conflicts between env and scriptthing variables."""
    if config is None:
        config = get_or_create_config()
    
    return config.get("variable_preference", "env")


def get_auto_generate_bindings(config: Optional[Dict[str, Any]] = None) -> bool:
    """Get whether to automatically generate IDE binding files when variables change."""
    if config is None:
        config = get_or_create_config()
    
    return config.get("auto_generate_bindings", True)


def get_single_arg_convenience(config: Optional[Dict[str, Any]] = None) -> bool:
    """Get whether to enable single argument convenience for bash scripts."""
    if config is None:
        config = get_or_create_config()
    
    return config.get("single_arg_convenience", True)
