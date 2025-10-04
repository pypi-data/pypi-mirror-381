"""
Resource handling for scriptthing templates and config files.

This module provides robust access to package resources that works in both
development and installed package environments.
"""

from pathlib import Path
import sys

from jinja2 import Environment, FileSystemLoader, Template, select_autoescape

# Try to use importlib.resources (Python 3.9+) or importlib_resources backport
try:
    if sys.version_info >= (3, 9):
        import importlib.resources as resources
    else:
        import importlib_resources as resources
    HAS_RESOURCES = True
except ImportError:
    HAS_RESOURCES = False
    resources = None


def get_template_path(template_name: str) -> Path:
    """
    Get the path to a template file.
    
    Args:
        template_name: Name of the template file (e.g., 'template.py', 'scriptthing-utils.js')
        
    Returns:
        Path to the template file
    """
    if HAS_RESOURCES:
        try:
            # Use importlib.resources for installed packages
            with resources.as_file(resources.files('scriptthing.templates').joinpath(template_name)) as path:
                return Path(path)
        except (AttributeError, FileNotFoundError):
            pass
    
    # Fallback to filesystem path (development mode)
    template_dir = Path(__file__).parent.parent / "templates"
    template_path = template_dir / template_name
    
    if template_path.exists():
        return template_path
    else:
        raise FileNotFoundError(f"Template '{template_name}' not found in {template_dir}")


def get_config_path(config_name: str) -> Path:
    """
    Get the path to a config file.
    
    Args:
        config_name: Name of the config file (e.g., 'default_config.toml')
        
    Returns:
        Path to the config file
    """
    if HAS_RESOURCES:
        try:
            # Use importlib.resources for installed packages
            with resources.as_file(resources.files('scriptthing.config').joinpath(config_name)) as path:
                return Path(path)
        except (AttributeError, FileNotFoundError):
            pass
    
    # Fallback to filesystem path (development mode)
    config_dir = Path(__file__).parent.parent / "config"
    config_path = config_dir / config_name
    
    if config_path.exists():
        return config_path
    else:
        raise FileNotFoundError(f"Config '{config_name}' not found in {config_dir}")


def read_template(template_name: str) -> str:
    """
    Read a template file and return its contents.
    
    Args:
        template_name: Name of the template file
        
    Returns:
        Contents of the template file as a string
    """
    if HAS_RESOURCES:
        try:
            # Use importlib.resources for installed packages
            return resources.files('scriptthing.templates').joinpath(template_name).read_text()
        except (AttributeError, FileNotFoundError):
            pass
    
    # Fallback to filesystem read
    template_path = get_template_path(template_name)
    return template_path.read_text()


def get_templates_directory() -> Path:
    """
    Get the templates directory path.
    
    Returns:
        Path to the templates directory
    """
    if HAS_RESOURCES:
        try:
            # For installed packages, we need to extract to a temporary location
            # This is more complex, so we'll use the fallback approach
            pass
        except (AttributeError, FileNotFoundError):
            pass
    
    # Use filesystem path
    return Path(__file__).parent.parent / "templates"


def list_templates() -> list[str]:
    """
    List all available templates.
    
    Returns:
        List of template filenames
    """
    if HAS_RESOURCES:
        try:
            # Use importlib.resources for installed packages
            template_files = resources.files('scriptthing.templates')
            return [f.name for f in template_files.iterdir() if f.is_file()]
        except (AttributeError, FileNotFoundError):
            pass
    
    # Fallback to filesystem listing
    templates_dir = get_templates_directory()
    if templates_dir.exists():
        return [f.name for f in templates_dir.iterdir() if f.is_file()]
    else:
        return []


def get_template(name: str) -> Template:
    env = Environment(
        loader=FileSystemLoader(str(get_templates_directory())),
        autoescape=select_autoescape()
    )

    return env.get_template(name)
