"""
Test runner for scriptthing scripts
"""
import subprocess
import sys
import os
from pathlib import Path

def run_scriptthing_test(script_path):
    """Run a scriptthing test script using scriptthing-run"""
    result = subprocess.run([
        "scriptthing-run", str(script_path)
    ], capture_output=True, text=True, env={
        **os.environ, 
        "PATH": "/home/ubuntu/.local/bin:" + os.environ.get("PATH", "")
    })
    return result

def test_cli_basic():
    """Test basic scriptthing CLI functionality"""
    script_path = Path(__file__).parent / "test_cli_basic.py"
    result = run_scriptthing_test(script_path)
    
    assert result.returncode == 0, f"CLI basic test failed: {result.stderr}\nStdout: {result.stdout}"
    assert "✓ Basic CLI test passed" in result.stdout

def test_script_creation():
    """Test scriptthing script creation functionality"""
    script_path = Path(__file__).parent / "test_script_run.py"
    result = run_scriptthing_test(script_path)
    
    assert result.returncode == 0, f"Script creation test failed: {result.stderr}\nStdout: {result.stdout}"
    assert "✓ Script creation test passed" in result.stdout

# Note: test_imports.py runs as regular pytest (not scriptthing-run) since it's testing imports