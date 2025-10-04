#!/usr/bin/env scriptthing-run
#file: test_script_run.py
#lang: python
#desc: Test creating scriptthing scripts

import scriptthing
import subprocess
import sys
import uuid

# Create a unique script name
unique_name = f"createtest_{uuid.uuid4().hex[:8]}"

# Create a Python script
create_result = subprocess.run([
    sys.executable, "-m", "scriptthing", "new", "--no-edit", "py", unique_name
], capture_output=True, text=True)

assert create_result.returncode == 0, f"Python script creation failed: {create_result.stderr}"
assert unique_name in create_result.stdout, f"Script name not in output: {create_result.stdout}"

# Create a shell script
shell_name = f"shelltest_{uuid.uuid4().hex[:8]}"

shell_create_result = subprocess.run([
    sys.executable, "-m", "scriptthing", "new", "--no-edit", "sh", shell_name
], capture_output=True, text=True)

assert shell_create_result.returncode == 0, f"Shell script creation failed: {shell_create_result.stderr}"
assert shell_name in shell_create_result.stdout, f"Shell script name not in output: {shell_create_result.stdout}"



print("✓ Script creation test passed")