from subprocess import run as _run
import os
from pathlib import Path
from ..config.config import get_or_create_config

def open_editor(script: Path):
    _config = get_or_create_config()
    _editor = _config.get("editor", os.environ.get("EDITOR", None))
    if not _editor:
        raise RuntimeError("No configured editor")
    _run([_editor, script.name], cwd=script.parent)


