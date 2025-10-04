#!/usr/bin/env scriptthing-run
#file: test_cli_basic.py
#lang: python
#desc: Test basic scriptthing CLI functionality

import scriptthing
import subprocess
import sys
import uuid
from typing import Any

# Test help command
help_result: subprocess.CompletedProcess[str] = subprocess.run([
    sys.executable, "-m", "scriptthing", "--help"
], capture_output=True, text=True)

assert help_result.returncode == 0, f"Help command failed: {help_result.stderr}"
assert "scriptthing" in help_result.stdout, "Help output doesn't contain 'scriptthing'"

# Test config command
config_result: subprocess.CompletedProcess[str] = subprocess.run([
    sys.executable, "-m", "scriptthing", "config"
], capture_output=True, text=True)

assert config_result.returncode == 0, f"Config command failed: {config_result.stderr}"

# Test vars commands
test_key: str = f"test_key_{uuid.uuid4().hex[:8]}"
test_value: str = "test_value_123"

# Set a variable
set_result: subprocess.CompletedProcess[str] = subprocess.run([
    sys.executable, "-m", "scriptthing", "vars", "set", test_key, test_value
], capture_output=True, text=True)

assert set_result.returncode == 0, f"Vars set command failed: {set_result.stderr}"

# Get the variable
get_result: subprocess.CompletedProcess[str] = subprocess.run([
    sys.executable, "-m", "scriptthing", "vars", "get", test_key
], capture_output=True, text=True)

assert get_result.returncode == 0, f"Vars get command failed: {get_result.stderr}"
assert test_value in get_result.stdout, f"Expected '{test_value}' in output: {get_result.stdout}"

# Clean up
delete_result: subprocess.CompletedProcess[str] = subprocess.run([
    sys.executable, "-m", "scriptthing", "vars", "delete", test_key
], capture_output=True, text=True)

print("✓ Basic CLI test passed")