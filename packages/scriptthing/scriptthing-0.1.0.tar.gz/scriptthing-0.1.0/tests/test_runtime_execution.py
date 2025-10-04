import subprocess
import sys
import uuid
from pathlib import Path
import os

from scriptthing.templating.paths import get_script_by_name


def test_scriptthing_runtime_execution():
    """Create a Python script with `scriptthing new` and execute it using the runtime."""
    # Create a unique script name to avoid collisions between test runs
    script_name = f"runtimetest_{uuid.uuid4().hex[:8]}"

    # Use the scriptthing CLI to generate a new Python script without opening an editor
    create_proc = subprocess.run([
        sys.executable,
        "-m",
        "scriptthing",
        "new",
        "--no-edit",
        "py",
        script_name,
    ], capture_output=True, text=True)

    # Ensure the script was created successfully
    assert create_proc.returncode == 0, f"Failed to create script: {create_proc.stderr}"
    assert script_name in create_proc.stdout, "Script name was not reported in the CLI output."

    # Locate the created script using scriptthing's helper (respects user config)
    script_path: Path = get_script_by_name(script_name)
    assert script_path is not None and script_path.exists(), "Created script file was not found on disk."

    # Execute the script using the scriptthing runtime module
    run_proc = subprocess.run([
        "scriptthing-run",
        str(script_path),
    ], capture_output=True, text=True, env={
        **os.environ,
        "PATH": str(Path.home() / ".local/bin") + os.pathsep + os.environ.get("PATH", "")
    })

    # Validate successful execution and expected output from the template script
    assert run_proc.returncode == 0, f"Runtime execution failed: {run_proc.stderr}"
    assert "Hello from Python script!" in run_proc.stdout, "Expected greeting not found in runtime output."