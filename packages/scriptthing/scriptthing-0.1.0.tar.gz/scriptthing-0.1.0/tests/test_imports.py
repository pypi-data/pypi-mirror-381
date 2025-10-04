"""
Test that all critical scriptthing imports work correctly
"""

def test_core_imports():
    """Test that core scriptthing modules can be imported"""
    
    # Test main scriptthing import
    import scriptthing
    assert scriptthing is not None
    
    # Test CLI imports
    from scriptthing.cli import cli
    assert cli is not None
    
    # Test compiler imports (analyzers moved here)
    try:
        from scriptthing.compiler.analyzers import AnalysisContext
        assert AnalysisContext is not None
    except ImportError as e:
        pytest.fail(f"Failed to import AnalysisContext: {e}")
    
    # Test runtime modules (shebang moved here)
    from scriptthing.runtime import execution
    assert execution is not None
    
    # stack_tracer module was removed as part of legacy cleanup

def test_optional_imports():
    """Test optional imports don't break the package"""
    
    # MCP should be optional
    try:
        from scriptthing.mcp import UniversalMCPMetadataParser
        # If it imports, that's fine
    except ImportError:
        # If it doesn't import, that's also fine since it's optional
        pass