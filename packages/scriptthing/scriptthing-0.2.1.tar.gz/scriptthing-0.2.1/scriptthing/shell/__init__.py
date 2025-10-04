from subprocess import run as _run
import os
from pathlib import Path
from ..config.config import get_or_create_config

def open_editor(script: Path | list[Path], layout: str = "auto"):
    """
    Open editor with specified files and layout.
    
    Args:
        script: Single file path or list of file paths
        layout: Layout mode - "auto", "splits", "tabs", or "standard"
    """
    _config = get_or_create_config()
    _editor = os.environ.get("EDITOR", None) or _config.editor
    if not _editor:
        raise RuntimeError("No configured editor")
    
    # Detect if editor supports vim-style options
    editor_name = os.path.basename(_editor).lower()
    supports_vim_options = editor_name in ['vim', 'nvim', 'gvim', 'vimx']
    
    if isinstance(script, list):
        if len(script) == 1:
            # Single file - use original behavior
            _run([_editor, script[0].name], cwd=script[0].parent)
            return
        
        # Multiple files - determine layout
        if layout == "standard" or not supports_vim_options:
            # Standard mode - just pass all files to editor
            cmd = [_editor] + [str(s) for s in script]
        elif layout == "splits":
            # Force splits
            cmd = [_editor, "-o"] + [str(s) for s in script]
        elif layout == "tabs":
            # Force tabs
            cmd = [_editor, "-p"] + [str(s) for s in script]
        else:  # layout == "auto"
            # Auto mode - use splits for 2 files, tabs for 3+
            if len(script) == 2:
                cmd = [_editor, "-o"] + [str(s) for s in script]
            else:  # 3+ files
                cmd = [_editor, "-p"] + [str(s) for s in script]
        
        _run(cmd)
    else:
        # Single file - original behavior
        _run([_editor, script.name], cwd=script.parent)


