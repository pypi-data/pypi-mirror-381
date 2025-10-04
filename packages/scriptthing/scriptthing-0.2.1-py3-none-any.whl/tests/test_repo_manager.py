"""
Unit tests for the ScriptRepo repository management functionality.

This module tests the ScriptRepo.find_script() method and related functionality
to ensure robust file-finding logic across all repository directories.
"""

import pytest
import tempfile
from pathlib import Path
from scriptthing.repo.manager import ScriptRepo


@pytest.fixture
def temp_repo():
    """
    Create a temporary repository structure for testing.
    
    Creates the following structure:
    - scripts/my_script.py
    - functions/my_func.sh  
    - extensions/my_ext.sh
    - dotfiles/.bashrc
    - dotfiles/config.yaml
    - bin/ (empty, for symlinks)
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        repo_path = Path(tmpdir)
        
        # Create directory structure
        scripts_dir = repo_path / "scripts"
        functions_dir = repo_path / "functions"
        extensions_dir = repo_path / "extensions"
        dotfiles_dir = repo_path / "dotfiles"
        bin_dir = repo_path / "bin"
        
        for dir_path in [scripts_dir, functions_dir, extensions_dir, dotfiles_dir, bin_dir]:
            dir_path.mkdir(parents=True)
        
        # Create test files
        (scripts_dir / "my_script.py").write_text("#!/usr/bin/env python3\nprint('Hello from script')")
        (scripts_dir / "another_script.sh").write_text("#!/bin/bash\necho 'Hello from shell script'")
        (functions_dir / "my_func.sh").write_text("#!/bin/bash\nmy_func() { echo 'Hello from function'; }")
        (extensions_dir / "my_ext.sh").write_text("#!/bin/bash\nexport MY_EXTENSION=true")
        (dotfiles_dir / ".bashrc").write_text("# Bash configuration\nPS1='$ '")
        (dotfiles_dir / "config.yaml").write_text("app:\n  name: test\n  version: 1.0")
        (dotfiles_dir / "settings.json").write_text('{"theme": "dark", "font": "mono"}')
        
        # Create a ScriptRepo instance
        repo = ScriptRepo(
            root=repo_path,
            name="test_repo",
            scripts_dir=scripts_dir,
            functions_dir=functions_dir,
            extensions_dir=extensions_dir,
            bin_dir=bin_dir,
            dotfiles_dir=dotfiles_dir
        )
        
        yield repo


class TestScriptRepoFindScript:
    """Test cases for ScriptRepo.find_script() method."""
    
    def test_find_script_in_scripts_directory(self, temp_repo):
        """Test finding a Python script in the scripts directory."""
        result = temp_repo.find_script("my_script")
        assert result is not None
        assert result.name == "my_script.py"
        assert result.parent == temp_repo.scripts_dir
        assert result.exists()
        assert "Hello from script" in result.read_text()
    
    def test_find_script_with_extension_in_scripts_directory(self, temp_repo):
        """Test finding a shell script in the scripts directory."""
        result = temp_repo.find_script("another_script")
        assert result is not None
        assert result.name == "another_script.sh"
        assert result.parent == temp_repo.scripts_dir
        assert result.exists()
        assert "Hello from shell script" in result.read_text()
    
    def test_find_function_in_functions_directory(self, temp_repo):
        """Test finding a shell function in the functions directory."""
        result = temp_repo.find_script("my_func")
        assert result is not None
        assert result.name == "my_func.sh"
        assert result.parent == temp_repo.functions_dir
        assert result.exists()
        assert "my_func()" in result.read_text()
    
    def test_find_extension_in_extensions_directory(self, temp_repo):
        """Test finding a shell extension in the extensions directory."""
        result = temp_repo.find_script("my_ext")
        assert result is not None
        assert result.name == "my_ext.sh"
        assert result.parent == temp_repo.extensions_dir
        assert result.exists()
        assert "MY_EXTENSION=true" in result.read_text()
    
    def test_find_dotfile_by_name(self, temp_repo):
        """Test finding a dotfile by its name."""
        result = temp_repo.find_script(".bashrc")
        assert result is not None
        assert result.name == ".bashrc"
        assert result.parent == temp_repo.dotfiles_dir
        assert result.exists()
        assert "Bash configuration" in result.read_text()
    
    def test_find_dotfile_without_dot_prefix(self, temp_repo):
        """Test finding a dotfile without the dot prefix."""
        result = temp_repo.find_script("bashrc")
        assert result is not None
        assert result.name == ".bashrc"
        assert result.parent == temp_repo.dotfiles_dir
        assert result.exists()
    
    def test_find_dotfile_with_extension(self, temp_repo):
        """Test finding a dotfile with extension."""
        result = temp_repo.find_script("config")
        assert result is not None
        assert result.name == "config.yaml"
        assert result.parent == temp_repo.dotfiles_dir
        assert result.exists()
        assert "app:" in result.read_text()
    
    def test_find_dotfile_with_json_extension(self, temp_repo):
        """Test finding a dotfile with JSON extension."""
        result = temp_repo.find_script("settings")
        assert result is not None
        assert result.name == "settings.json"
        assert result.parent == temp_repo.dotfiles_dir
        assert result.exists()
        assert '"theme": "dark"' in result.read_text()
    
    def test_find_nonexistent_script(self, temp_repo):
        """Test searching for a script that does not exist."""
        result = temp_repo.find_script("nonexistent_script")
        assert result is None
    
    def test_find_script_case_sensitive(self, temp_repo):
        """Test that script finding is case sensitive."""
        result = temp_repo.find_script("My_Script")  # Different case
        assert result is None
        
        result = temp_repo.find_script("my_script")  # Correct case
        assert result is not None
        assert result.name == "my_script.py"
    
    def test_find_script_priority_order(self, temp_repo):
        """Test that the search follows the correct priority order."""
        # Create a file with the same name in multiple directories
        # to test priority order
        (temp_repo.functions_dir / "priority_test.sh").write_text("#!/bin/bash\necho 'function'")
        (temp_repo.extensions_dir / "priority_test.sh").write_text("#!/bin/bash\necho 'extension'")
        
        # Should find the one in scripts directory first (highest priority)
        result = temp_repo.find_script("priority_test")
        assert result is not None
        # Since we don't have one in scripts, it should find the first one
        # in the search order (functions before extensions)
        assert result.parent == temp_repo.functions_dir
    
    def test_find_script_with_symlink_in_bin(self, temp_repo):
        """Test finding a script via symlink in bin directory."""
        # Create a symlink in bin directory
        target_script = temp_repo.scripts_dir / "my_script.py"
        bin_link = temp_repo.bin_dir / "my_script"
        bin_link.symlink_to(target_script)
        
        # Should find the symlink in bin directory
        result = temp_repo.find_script("my_script")
        # The method should find the actual file in scripts directory first
        # before checking bin directory, so this should still return the scripts version
        assert result is not None
        assert result.name == "my_script.py"
        assert result.parent == temp_repo.scripts_dir
    
    def test_find_script_empty_directories(self, temp_repo):
        """Test finding scripts when some directories are empty."""
        # Remove all files from functions directory
        for file in temp_repo.functions_dir.glob("*"):
            file.unlink()
        
        # Should still find scripts in other directories
        result = temp_repo.find_script("my_script")
        assert result is not None
        assert result.name == "my_script.py"
        assert result.parent == temp_repo.scripts_dir
    
    def test_find_script_nonexistent_directories(self, temp_repo):
        """Test finding scripts when some directories don't exist."""
        # Remove the functions directory entirely
        import shutil
        shutil.rmtree(temp_repo.functions_dir)
        
        # Should still find scripts in other directories
        result = temp_repo.find_script("my_script")
        assert result is not None
        assert result.name == "my_script.py"
        assert result.parent == temp_repo.scripts_dir
        
        # Should not find anything in the removed directory
        result = temp_repo.find_script("my_func")
        assert result is None


class TestScriptRepoValidation:
    """Test cases for ScriptRepo Pydantic validation."""
    
    def test_script_repo_validation_with_nonexistent_root(self):
        """Test that ScriptRepo validation fails with nonexistent root."""
        with pytest.raises(ValueError, match="Repository root directory does not exist"):
            ScriptRepo(
                root=Path("/nonexistent/path"),
                name="test",
                scripts_dir=Path("/nonexistent/scripts"),
                functions_dir=Path("/nonexistent/functions"),
                extensions_dir=Path("/nonexistent/extensions"),
                bin_dir=Path("/nonexistent/bin"),
                dotfiles_dir=Path("/nonexistent/dotfiles")
            )
    
    def test_script_repo_validation_with_valid_root(self, temp_repo):
        """Test that ScriptRepo validation passes with valid root."""
        # The temp_repo fixture already creates a valid repo
        assert temp_repo.root.exists()
        assert temp_repo.name == "test_repo"
        assert temp_repo.scripts_dir.exists()
        assert temp_repo.functions_dir.exists()
        assert temp_repo.extensions_dir.exists()
        assert temp_repo.bin_dir.exists()
        assert temp_repo.dotfiles_dir.exists()