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
    
    # Compiler and runtime modules have been removed for simplification
    
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