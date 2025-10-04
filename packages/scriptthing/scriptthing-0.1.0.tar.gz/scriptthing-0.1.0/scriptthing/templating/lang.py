from pathlib import Path
from typing import Dict
from .resources import get_template_path, get_templates_directory

_template_path: Path = get_templates_directory()

languages: Dict[str, Path] = {
    "sh": _template_path/"template.sh",
    "py": _template_path/"template.py", 
    "function": _template_path/"function.sh",  # Shell functions (only sourced in bash scripts)
    "extension": _template_path/"extension.sh",  # Shell extensions (always sourced)
}


