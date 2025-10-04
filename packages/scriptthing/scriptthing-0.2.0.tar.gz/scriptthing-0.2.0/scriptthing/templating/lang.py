from pathlib import Path
from typing import Dict
from .resources import get_template_path, get_templates_directory

_template_path: Path = get_templates_directory()

languages: Dict[str, Path] = {
    "sh": _template_path/"template.sh",           # Standard bash script
    "py": _template_path/"template.py",           # Standard python script
    "arg": _template_path/"template.arg",         # Argorator script (bash with argorator shebang)
    "scr": _template_path/"template.scr",         # ScriptThing script (python with scriptthing-run shebang)
    "script": _template_path/"template.script",   # ScriptThing script (python with scriptthing-run shebang)
    "function": _template_path/"function.sh",     # Shell functions (only sourced in bash scripts)
    "extension": _template_path/"extension.sh",   # Shell extensions (always sourced)
    "module": _template_path/"template.module",   # Python module
}


