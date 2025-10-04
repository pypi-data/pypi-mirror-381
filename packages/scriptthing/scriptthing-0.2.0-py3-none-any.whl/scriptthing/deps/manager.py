from __future__ import annotations

import shutil
import subprocess
from pathlib import Path
from typing import Iterable


def ensure_repo_venv(repo_root: Path) -> tuple[Path, Path]:
    """Ensure <repo>/.venv exists. Try stdlib venv, then virtualenv fallback.
    Returns (python_bin, venv_dir).
    """
    venv_dir = repo_root / ".venv"
    python_bin = venv_dir / "bin" / "python"
    if not python_bin.exists():
        subprocess.run(["python3", "-m", "venv", str(venv_dir)], check=False)
        if not python_bin.exists():
            venv_cmd = shutil.which("virtualenv")
            if venv_cmd:
                subprocess.run([venv_cmd, str(venv_dir)], check=False)
            else:
                subprocess.run(["python3", "-m", "virtualenv", str(venv_dir)], check=False)
    return python_bin, venv_dir


def ensure_pip_in_venv(venv_python: Path) -> None:
    """Ensure pip is present in the given venv Python by invoking get-pip.py if needed."""
    try:
        res = subprocess.run([str(venv_python), "-m", "pip", "--version"], capture_output=True)
        if res.returncode == 0:
            return
    except Exception:
        pass
    try:
        import tempfile, urllib.request
        with tempfile.TemporaryDirectory() as td:
            gp = Path(td) / "get-pip.py"
            urllib.request.urlretrieve("https://bootstrap.pypa.io/get-pip.py", gp)
            subprocess.run([str(venv_python), str(gp), "--no-warn-script-location"], check=False)
    except Exception:
        pass


def install_requirements_txt(repo_root: Path, req_file: Path) -> None:
    python_bin, _ = ensure_repo_venv(repo_root)
    ensure_pip_in_venv(python_bin)
    subprocess.run([str(python_bin), "-m", "pip", "install", "-r", str(req_file)], cwd=str(repo_root))


def install_explicit_requirements(repo_root: Path, requirements: Iterable[str]) -> None:
    python_bin, _ = ensure_repo_venv(repo_root)
    ensure_pip_in_venv(python_bin)
    for req in requirements:
        subprocess.run([str(python_bin), "-m", "pip", "install", req], cwd=str(repo_root))

