import sys
from contextlib import contextmanager
from .analyzer import ErrorAnalyzer
from .formatter import ErrorFormatter


class AIDebugger:
    """Main AI debugger class."""
    
    def __init__(self, use_color=True, show_original_traceback=False):
        self.analyzer = ErrorAnalyzer()
        self.formatter = ErrorFormatter(use_color=use_color)
        self.original_excepthook = None
        self.enabled = False
        self.show_original_traceback = show_original_traceback
    
    def exception_handler(self, exc_type, exc_value, exc_traceback):
        """Custom exception handler that provides AI debugging."""
        try:
            # Analyze the error
            analysis = self.analyzer.analyze_exception(exc_type, exc_value, exc_traceback)
            
            # Format and display
            self.formatter.format_error(analysis)
            
            # Optionally show original traceback
            if self.show_original_traceback and self.original_excepthook:
                self.original_excepthook(exc_type, exc_value, exc_traceback)
        
        except Exception as format_error:
            # If AI-DBUG itself has an error, fall back to original exception handler
            print("\n[AI-DBUG encountered an error while formatting. Showing original error:]\n")
            if self.original_excepthook:
                self.original_excepthook(exc_type, exc_value, exc_traceback)
            else:
                # Last resort: print the original error
                import traceback
                traceback.print_exception(exc_type, exc_value, exc_traceback)
    
    def enable(self):
        """Enable AI debugging."""
        if not self.enabled:
            self.original_excepthook = sys.excepthook
            sys.excepthook = self.exception_handler
            self.enabled = True
    
    def disable(self):
        """Disable AI debugging."""
        if self.enabled:
            sys.excepthook = self.original_excepthook
            self.enabled = False


# Global debugger instance
_global_debugger = None


def enable_ai_debugging(use_color=True, show_original_traceback=False):
    """
    Enable AI-powered debugging globally.
    
    Args:
        use_color: Whether to use colored output (default: True)
        show_original_traceback: Whether to show Python's default traceback (default: False)
    """
    global _global_debugger
    if _global_debugger is None:
        _global_debugger = AIDebugger(use_color=use_color, show_original_traceback=show_original_traceback)
    _global_debugger.enable()


def disable_ai_debugging():
    """Disable AI-powered debugging."""
    global _global_debugger
    if _global_debugger:
        _global_debugger.disable()


@contextmanager
def debug_context(use_color=True, show_original_traceback=False):
    """
    Context manager for AI debugging within a specific block.
    
    Usage:
        with debug_context():
            # Your code here
            risky_operation()
    """
    debugger = AIDebugger(use_color=use_color, show_original_traceback=show_original_traceback)
    debugger.enable()
    try:
        yield debugger
    finally:
        debugger.disable()


@contextmanager
def debug_multiple(use_color=True, show_original_traceback=False):
    """
    Context manager that catches and shows multiple errors without stopping.
    
    Usage:
        with debug_multiple():
            error1()  # Shows error but continues
            error2()  # Shows this error too
            error3()  # And this one
    """
    debugger = AIDebugger(use_color=use_color, show_original_traceback=show_original_traceback)
    formatter = ErrorFormatter(use_color=use_color)
    analyzer = ErrorAnalyzer()
    
    error_count = [0]  # Using list to modify in nested function
    
    class MultiErrorHandler:
        def __enter__(self):
            return self
        
        def __exit__(self, exc_type, exc_value, exc_traceback):
            if exc_type is not None:
                error_count[0] += 1
                analysis = analyzer.analyze_exception(exc_type, exc_value, exc_traceback)
                formatter.format_error(analysis)
                # Suppress the exception and continue
                return True
            return False
        
        def run(self, func, *args, **kwargs):
            """Run a function and catch its errors."""
            with self:
                func(*args, **kwargs)
        
        def get_error_count(self):
            """Get total number of errors caught."""
            return error_count[0]
    
    handler = MultiErrorHandler()
    try:
        yield handler
    finally:
        if error_count[0] > 0:
            print(f"\n{'='*70}")
            print(f"🐛 Total errors caught and explained: {error_count[0]}")
            print(f"{'='*70}\n")
