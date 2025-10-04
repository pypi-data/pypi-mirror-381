"""Simplified decorator-based compiler pipeline."""
from typing import Dict, List, Generator, Callable, Optional, Any, ContextManager
from pathlib import Path
from contextlib import ExitStack

from .context import CompilerContext
from .analyzers import analyze_script, AnalysisContext


# Global registry for compiler steps
_STEPS: Dict[str, Callable[[CompilerContext], Generator[None, None, None]]] = {}
_STEP_ORDER: List[str] = []
_NEXT_DEFAULT_ORDER: int = 100  # Auto-incrementing default order


def compiler_step(order: Optional[int] = None) -> Callable[[Callable[[CompilerContext], Generator[None, None, None]]], Callable[[CompilerContext], Generator[None, None, None]]]:
    """Decorator to register a compiler step with setup/teardown capability.
    
    Args:
        order: Execution order (lower numbers run first). If None, uses auto-incrementing default.
        
    Example:
        @compiler_step()  # Uses default order
        def my_step(context):
            yield
            
        @compiler_step(order=10)  # Explicit order
        def priority_step(context):
            yield
    """
    def decorator(func: Callable[[CompilerContext], Generator[None, None, None]]) -> Callable[[CompilerContext], Generator[None, None, None]]:
        global _NEXT_DEFAULT_ORDER
        
        step_name: str = func.__name__
        
        # Determine order
        if order is None:
            step_order: int = _NEXT_DEFAULT_ORDER
            _NEXT_DEFAULT_ORDER += 10  # Increment for next default step
        else:
            step_order = order
        
        # Store the step
        _STEPS[step_name] = func
        
        # Add to order list and sort
        if step_name not in _STEP_ORDER:
            _STEP_ORDER.append(step_name)
        
        # Sort by order (using a simple approach)
        def get_order(step_name: str) -> int:
            # Store order as function attribute
            if hasattr(_STEPS[step_name], '_order'):
                return _STEPS[step_name]._order
            return 100
        
        # Set order on function
        func._order = step_order  # type: ignore
        _STEP_ORDER.sort(key=get_order)
        
        return func
    
    return decorator


def run_pipeline(script_path: Path) -> tuple[str, AnalysisContext]:
    """Run the compiler pipeline on a script.
    
    Args:
        script_path: Path to the script to compile
        
    Returns:
        Tuple of (compiled_content, analysis_context)
    """
    # Run analysis first
    analysis_context: AnalysisContext = analyze_script(script_path)
    
    # Create compiler context
    context: CompilerContext = CompilerContext(script_path, analysis_context)
    
    # Run all steps using context managers
    with ExitStack() as stack:
        for step_name in _STEP_ORDER:
            step_func: Callable[[CompilerContext], Generator[None, None, None]] = _STEPS[step_name]
            cm: ContextManager[None] = _create_step_context_manager(step_func, context)
            stack.enter_context(cm)
    
    return context.content, analysis_context


def _create_step_context_manager(step_func: Callable[[CompilerContext], Generator[None, None, None]], context: CompilerContext) -> ContextManager[None]:
    """Create a context manager for a step function."""
    from contextlib import contextmanager
    
    @contextmanager
    def step_cm() -> Generator[None, None, None]:
        generator: Generator[None, None, None] = step_func(context)
        try:
            # Run setup (before yield)
            next(generator)
            yield
        except StopIteration:
            # No yield in function
            yield
        finally:
            try:
                # Run teardown (after yield)
                next(generator)
            except StopIteration:
                pass
    
    return step_cm()


def list_steps() -> List[str]:
    """Get list of registered steps in execution order."""
    return _STEP_ORDER.copy()


def get_step_info() -> Dict[str, Dict[str, Any]]:
    """Get information about all registered steps."""
    return {
        name: {
            'order': getattr(_STEPS[name], '_order', 100),
            'name': name
        }
        for name in _STEP_ORDER
    }