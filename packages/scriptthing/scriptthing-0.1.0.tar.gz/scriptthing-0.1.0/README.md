# 🛠️ ScriptThing

> **A modern, opinionated toolkit for creating, managing, and sharing scripts across Python and Bash**

[![PyPI version](https://img.shields.io/pypi/v/scriptthing.svg)](https://pypi.org/project/scriptthing/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![CI](https://github.com/scriptthing/scriptthing/actions/workflows/simple-tests.yml/badge.svg)](https://github.com/scriptthing/scriptthing/actions)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)

**ScriptThing** transforms the way you work with scripts by providing a unified toolkit that handles the boring parts—CLI parsing, output formatting, cross-language bindings, packaging, deployment, and now repo-scoped management—so you can focus on writing code that matters.

---

## ✨ Why ScriptThing?

- 🚀 **Instant scaffolding** — `scriptthing new py my_tool` creates a fully-featured script in seconds
- 🔄 **Language agnostic** — Same workflow for Python and Bash
- 📊 **Rich output** — JSON, CSV, Markdown, HTML, XML, YAML with simple helpers
- 🔗 **Cross-language bindings** — Call any script from any language seamlessly
- 🤖 **AI-ready** — Expose scripts as AI tools via Model Context Protocol (MCP)
- 🎯 **Type-safe** — Automatic type inference and validation for script parameters
- 📦 **Zero-config packaging** — Scripts are immediately executable and shareable
- 🔧 **Powerful templating** — Jinja2-powered templates for complex script generation

---

## 🚀 Quick Start

### Installation

```bash
# Install from PyPI (recommended)
pip install scriptthing

# Development install
git clone https://github.com/scriptthing/scriptthing.git
cd scriptthing
pip install -e .

# In restricted environments
pip install -e . --break-system-packages

# If command not found, run via module or add to PATH
python -m scriptthing --help
export PATH="$PATH:$HOME/.local/bin"
```

**Requirements:** Python ≥ 3.12  
**Optional:** `fastmcp` (AI/MCP), `PyYAML` (YAML)

### Repo Model (New)

ScriptThing now uses repo-scoped management by default:

- Each repo has: `scriptthing.toml`, `scripts/`, `functions/`, `bin/` (symlinks to scripts), `modules/`, `.venv/`, `.st/`
- A default repo is auto-created at `~/.config/scriptthing/repo`
- `eval "$(scriptthing install)"` adds each repo’s `bin/` to PATH (when `add_bin_to_path = true`) and sources functions

Repo selection for `new`/`edit`:
1. `--repo <name|path>`
2. `ST_DEFAULT_REPO` variable (set via `scriptthing vars set ST_DEFAULT_REPO /path|name`)
3. Default repo

Dependencies:
- `requirements.txt` in repo root installs into `.venv`
- Scripts can declare explicit `# requires: <pip-spec>` lines; these are installed on execution
- Pre-install across repo: `scriptthing repos install-explicit [--repo]`
- Venv creation falls back to `virtualenv` if stdlib venv is blocked; if pip is missing in venv, we bootstrap with get-pip.py (repo-local only)

Bindings:
- Generated to `<repo>/modules/bindings.py` via `scriptthing generate bindings`
- Import default repo bindings: `from scriptthing.bindings import my_script`
- Import other repos by namespace (sanitized repo name): `from scriptthing.bindings.my_repo import my_script`

Top-level modules (optional, per-module):
- Place packages/modules in `<repo>/modules`
- Install a single module to top-level in repo venv: `scriptthing modules install mypkg --repo <repo>`; then `import mypkg` inside that venv

### Your First Script

```bash
# Create a new Python script
scriptthing new py hello_world

# This creates a fully-featured script with:
# ✓ Shebang (#!/usr/bin/env scriptthing-run)
# ✓ Optional MCP metadata block
# ✓ Imports and main structure
```

The generated script:
```python
#!/usr/bin/env scriptthing-run
# lang: py

# MCP Metadata (uncomment and modify for MCP support):
# MCP_NAME: hello_world
# MCP_DESCRIPTION: A friendly greeting script
# MCP_PARAM: name:string:Name to greet:true

from scriptthing import stdin

def main():
    print("Hello from Python script!")

if __name__ == "__main__":
    main()
```

### Run and Manage

```bash
# Add repo bins to PATH for your shell
eval "$(scriptthing install)"

# Run your script (from repo bin)
hello_world

# List all scripts
scriptthing ls

# Edit a script
scriptthing edit hello_world

# Remove a script
scriptthing rm hello_world

# Import an existing file as a script
scriptthing import ./some_tool.py

# Show compiled script
scriptthing compile my_script

# Generate Python bindings
scriptthing generate bindings

# Generate MCP server and config
scriptthing generate mcp
scriptthing generate mcp-config

# Parallel streaming over input
cat data.txt | scriptthing stream 'echo {_1}:{_2}' -s ':'

# Manage variables
scriptthing vars set API_KEY "secret123" --ttl 1h
scriptthing vars show
scriptthing vars get API_KEY
scriptthing vars auto-bindings status
```

---

## 🏗️ Core Features

### 📝 Multi-Language Support

Create scripts in your preferred language with consistent tooling:

```bash
# Python scripts with rich data processing
scriptthing new py data_processor

# Shell scripts for system automation  
scriptthing new sh system_backup

# Shell script for system tasks
scriptthing new sh system_monitor

# Reusable shell functions
scriptthing new function deploy_app
```

### 📊 Output Formatting (Python)

Transform data with a simple, chainable API:

```python
from scriptthing.output import from_dict, from_table

# Single objects
user = from_dict({"name": "Alice", "age": 30, "role": "developer"})
print(user.as_json())           # JSON output
print(user.as_yaml())           # YAML output
print(user.as_html())           # HTML table

# Collections and tables
users = from_table([
    {"name": "Alice", "age": 30, "role": "developer"},
    {"name": "Bob", "age": 25, "role": "designer"},
    {"name": "Charlie", "age": 35, "role": "manager"}
])

# Chain operations for data processing
seniors = (users
    .filter(lambda u: u["age"] > 28)
    .sort("name")
    .select(["name", "role"]))

print(seniors.as_markdown())    # Markdown table
print(seniors.as_csv())         # CSV export
print(seniors.as_html())        # HTML table (options available)
```

**Supported formats:** Text, JSON, JSONL, CSV, TSV, XML, HTML, Markdown, YAML

### 🔗 Cross-Language Bindings

Call any script from Python with full type safety:

```bash
# Generate Python bindings for all scripts
scriptthing generate bindings
```

```python
# Import and use your scripts as Python functions
from scriptthing.bindings import data_processor, system_backup

# Type-safe calls with automatic parameter validation
result = data_processor(input_file="data.csv", format="json")
backup_status = system_backup(target_dir="/home/user", compress=True)
```

### 🤖 AI Integration (MCP)

Expose your scripts as AI tools using the Model Context Protocol:

```bash
# Generate MCP server from all scripts
scriptthing generate mcp

# Generate MCP configuration for Claude/other AI tools
scriptthing generate mcp-config

# Add MCP metadata to existing scripts
scriptthing generate mcp-metadata my_script
```

Your scripts become AI-callable tools:
```python
# In your script, add MCP metadata:
# MCP_NAME: file_analyzer
# MCP_DESCRIPTION: Analyze file structure and content
# MCP_PARAM: file_path:string:Path to analyze:true
# MCP_PARAM: include_hidden:boolean:Include hidden files:false
```

### 🗄️ Variables

Built-in key-value store for configuration and state:

```bash
# Set variables with optional TTL
scriptthing vars set API_KEY "secret123" --ttl 3600
scriptthing vars set DB_HOST "localhost"

# Use in scripts
scriptthing vars get API_KEY

# Setup language-specific environments
scriptthing vars setup python  # Sets up env if your repo modules need it
```

### ⚙️ Configuration

```bash
# View current configuration
scriptthing config

# Add repo bins to PATH and source functions
eval "$(scriptthing install)"
```

---

## 🎯 Advanced Usage

### Template Customization

ScriptThing ships with built-in templates for Python and Shell. You can edit generated scripts directly or build your own scaffolding in a repo.

### Script Compilation

View the compiled version of your scripts to understand the runtime behavior:

```bash
# See how scriptthing processes your script
scriptthing compile my_script
```

### Stdin Processing

ScriptThing provides powerful stdin utilities for all languages:

```python
# Python
from scriptthing import stdin

data = stdin.json()     # Parse JSON from stdin
lines = stdin.jsonl()   # Parse JSONL (one JSON per line)
text = stdin.text()     # Read plain text
csv_data = stdin.csv()  # Parse CSV with headers
```



```bash
# Shell (via environment variables set by scriptthing-run)
echo "$STDIN_JSON" | jq '.field'
cat "$STDIN_FILE" | head -10
```

---

## 📚 CLI Reference (Quick)

### Core Commands

| Command | Description | Example |
|---------|-------------|---------|
| `new` | Create a new script | `scriptthing new {py|sh|function} my_tool` |
| `ls` | List all scripts | `scriptthing ls` |
| `edit` | Open script in `$EDITOR` | `scriptthing edit my_script` |
| `rm` | Remove a script | `scriptthing rm old_script` |
| `compile` | Show compiled script | `scriptthing compile my_script` |
| `import` | Import an existing file as a script | `scriptthing import ./tool.sh` |
| `install` | Output shell code to source functions | `scriptthing install --help-text` |
| `stream` | Parallel streaming executor with templates | `scriptthing stream 'echo {_1}'` |

### Generation Commands

| Command | Description | Example |
|---------|-------------|---------|
| `generate bindings` | Create Python bindings | `scriptthing generate bindings` |
| `generate mcp` | Create MCP server | `scriptthing generate mcp` |
| `generate mcp-config` | Generate MCP config | `scriptthing generate mcp-config` |
| `generate mcp-metadata` | Add MCP metadata | `scriptthing generate mcp-metadata my_script` |

### Management Commands

| Command | Description | Example |
|---------|-------------|---------|
| `vars set` | Set a variable | `scriptthing vars set KEY value --ttl 1h` |
| `vars get` | Get a variable | `scriptthing vars get KEY` |
| `vars show` | Show all variables | `scriptthing vars show` |
| `vars delete` | Delete a variable | `scriptthing vars delete KEY` |
| `vars setup` | Run language-specific setup | `scriptthing vars setup python` |
| `vars generate-bindings` | Generate IDE stub file | `scriptthing vars generate-bindings` |
| `vars auto-bindings` | Toggle auto IDE binding generation | `scriptthing vars auto-bindings on` |
| `config` | Show configuration | `scriptthing config` |


---

## 🔧 Configuration

ScriptThing stores a single global config at `~/.config/scriptthing/config.toml` (editor, core settings). All scripts, bins, modules, and venvs live within repos. A default repo is created at `~/.config/scriptthing/repo` on first use.

---

## 🤝 Contributing

We welcome contributions! Here's how to get started:

1. **Fork and clone** the repository
2. **Install in development mode:** `pip install -e ".[dev]"`
3. **Run tests:** `pytest`
4. **Make your changes** and add tests
5. **Submit a pull request**

### Development Setup

```bash
git clone https://github.com/scriptthing/scriptthing.git
cd scriptthing

# Install with development dependencies
pip install -e ".[dev,test,mcp]"

# Install pre-commit hooks
pre-commit install

# Run tests
pytest tests/

# Test CLI changes
scriptthing --help
```

---

## 📖 Documentation

This README contains everything you need to install, create scripts, run them, format output, generate bindings, integrate MCP, manage variables, and use the parallel stream executor. Use `scriptthing --help` and subcommand `--help` flags for up-to-date usage details.

---

## 🎯 Roadmap

- [ ] **Web UI** - Browser-based script management
- [ ] **Docker integration** - Containerized script execution
- [ ] **Remote execution** - Run scripts on remote servers
- [ ] **Plugin system** - Extensible architecture
- [ ] **IDE extensions** - VS Code, PyCharm integration
- [ ] **Package registry** - Share scripts with the community

---

## 📄 License

ScriptThing is distributed under the **MIT License**. See [LICENSE](LICENSE) for details.

---

## ⭐ Star History

If ScriptThing has been helpful, please consider giving it a star on GitHub! It helps others discover the project.

[![Star History Chart](https://api.star-history.com/svg?repos=scriptthing/scriptthing&type=Date)](https://star-history.com/#scriptthing/scriptthing&Date)