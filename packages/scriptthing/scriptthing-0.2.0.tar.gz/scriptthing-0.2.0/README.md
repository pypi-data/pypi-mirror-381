# 🛠️ ScriptThing

[![PyPI version](https://img.shields.io/pypi/v/scriptthing.svg)](https://pypi.org/project/scriptthing/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

ScriptThing organizes your scripts, handles Python imports between them, and syncs your dotfiles.

---

## Why ScriptThing?

- Create scripts with proper structure instantly
- Share Python functions between scripts without packaging
- Keep scripts organized in repositories
- Sync dotfiles across machines
- Edit and manage everything from one command

---

## Quick Start

### Installation

```bash
# Install from PyPI (recommended)
pip install scriptthing

# Development install
git clone https://github.com/scriptthing/scriptthing.git
cd scriptthing
pip install -e .
```

**Requirements:** Python ≥ 3.10

### First Steps

```bash
# Create your first script
scriptthing new py hello_world

# Add ScriptThing to your shell PATH
eval "$(scriptthing install)"

# Your script is now available everywhere
hello_world
```

---

## Python Modules

Instead of copying functions between scripts or setting up proper Python packages, create simple modules:

```bash
# Create a reusable module
scriptthing new module my_utils
scriptthing edit my_utils

# Use it in any script
scriptthing new py data_processor
# data_processor.py can now: from my_utils import clean_data
```

Modules work across repositories and can be installed into any Python environment without packaging.

---

## Repository Structure

```
my-repo/
├── scripts/           # Executable scripts
├── modules/           # Python modules
├── dotfiles/          # Config files to sync
├── functions/         # Shell functions (sourced on demand)
├── extensions/        # Shell extensions (always sourced)
└── .venv/             # Python environment
```

---

## Commands

### Script Management
```bash
scriptthing new py my_tool           # Create Python script
scriptthing new sh deploy_app       # Create shell script  
scriptthing edit my_tool             # Edit script with smart layout
scriptthing edit script1 script2    # Edit multiple scripts (tabs/splits)
scriptthing ls                       # List all scripts
scriptthing rm my_tool               # Remove script
scriptthing import ./legacy_tool.py # Import existing script
```

### Repository Management

Repositories are collections of scripts, modules, and dotfiles. You can have multiple repositories for different projects or purposes.

ScriptThing creates a default repository at `~/.config/scriptthing/repo` for immediate use. Commands without `--repo` use this default.

```bash
scriptthing repos add /path/to/repo     # Add existing repository
scriptthing repos ls                    # List all repositories
scriptthing repos create ./new-repo     # Create new repository
scriptthing repos install <git-url>     # Install remote repository
scriptthing repos refresh               # Update symlinks and dependencies
```

### Dotfile Management
```bash
scriptthing dotfiles sync              # Sync dotfiles to home directory
scriptthing dotfiles status            # Show sync status
scriptthing dotfiles conflicts         # Check for conflicts
scriptthing dotfiles hotswap ~/.bashrc other-repo  # Switch versions
```

### Shell Integration
```bash
eval "$(scriptthing install)"          # Add to shell startup
scriptthing install --help-text        # Show installation instructions

# Shell extensions are sourced automatically on shell startup
scriptthing new extension my_aliases    # Create shell extension
scriptthing new function my_helper      # Create sourceable function
```

---

## Templates & Languages

ScriptThing includes built-in templates for common script types:

| Language | Command | Description |
|----------|---------|-------------|
| Python | `scriptthing new py name` | Standard Python script |
| Shell | `scriptthing new sh name` | Bash script with proper headers |
| Argorator | `scriptthing new arg name` | Shell with advanced argument parsing |
| Function | `scriptthing new function name` | Shell function (sourced) |
| Extension | `scriptthing new extension name` | Shell extension (always sourced) |
| Module | `scriptthing new module name` | Python module for reuse |

### Template Customization

Templates use Jinja2 and can be customized per repository. Create custom templates by adding them to your repository's template directory.

---

## Dotfiles

```bash
# Put config files in dotfiles/ directory
my-repo/dotfiles/.bashrc
my-repo/dotfiles/.vimrc

# Sync to home directory
scriptthing dotfiles sync
# Creates: ~/.bashrc -> /path/to/repo/dotfiles/.bashrc

# Handle conflicts when multiple repos have the same file
scriptthing dotfiles conflicts
scriptthing dotfiles hotswap ~/.bashrc preferred-repo
```

---

## Configuration

Repository config in `scriptthing.toml`:
```toml
[repo]
name = "my-scripts"
add_bin_to_path = true
```

Global config at `~/.config/scriptthing/config.toml`

---

## Advanced Features

```bash
# Edit multiple files with smart layouts
scriptthing edit script1 script2 --tabs

# Install Python packages to repository
scriptthing modules install requests --repo my-project

# Manage variables with expiration
scriptthing vars set API_KEY "secret" --ttl 1h
```

---

## Command Reference

| Command | Description |
|---------|-------------|
| `scriptthing new <type> <name>` | Create new script from template |
| `scriptthing edit <name>...` | Edit scripts with smart layouts |
| `scriptthing ls` | List all scripts, functions, extensions |
| `scriptthing rm <name>` | Remove script from repository |
| `scriptthing import <path>` | Import existing script |
| `scriptthing repos <cmd>` | Repository management commands |
| `scriptthing dotfiles <cmd>` | Dotfile synchronization commands |
| `scriptthing vars <cmd>` | Variable management commands |
| `scriptthing modules <cmd>` | Python module management |
| `scriptthing install` | Generate shell integration code |

---

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Development Setup
```bash
git clone https://github.com/scriptthing/scriptthing.git
cd scriptthing
pip install -e ".[test]"
pytest
```

---

## License

MIT License. See [LICENSE](LICENSE) for details.

---

**Ready to organize your scripts?** `pip install scriptthing` and start building! 🚀