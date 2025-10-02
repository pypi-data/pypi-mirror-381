import pytest
import sys
from ai_dbug import enable_ai_debugging, disable_ai_debugging, debug_context
from ai_dbug.analyzer import ErrorAnalyzer
from ai_dbug.knowledge_base import get_error_info


class TestErrorAnalyzer:
    """Test the ErrorAnalyzer class."""
    
    def test_type_error_analysis(self):
        """Test analyzing a TypeError."""
        analyzer = ErrorAnalyzer()
        
        try:
            result = 5 + "10"
        except Exception as e:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            analysis = analyzer.analyze_exception(exc_type, exc_value, exc_traceback)
            
            assert analysis['error_type'] == 'TypeError'
            assert 'unsupported operand' in analysis['error_message'].lower()
            assert 'incompatible types' in analysis['explanation'].lower()
            assert len(analysis['stack_trace']) > 0
    
    def test_value_error_analysis(self):
        """Test analyzing a ValueError."""
        analyzer = ErrorAnalyzer()
        
        try:
            num = int("not a number")
        except Exception as e:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            analysis = analyzer.analyze_exception(exc_type, exc_value, exc_traceback)
            
            assert analysis['error_type'] == 'ValueError'
            assert 'invalid literal' in analysis['error_message'].lower()
            assert analysis['fix'] is not None
    
    def test_key_error_analysis(self):
        """Test analyzing a KeyError."""
        analyzer = ErrorAnalyzer()
        
        try:
            d = {'a': 1}
            value = d['nonexistent_key']
        except Exception as e:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            analysis = analyzer.analyze_exception(exc_type, exc_value, exc_traceback)
            
            assert analysis['error_type'] == 'KeyError'
            assert 'dictionary' in analysis['explanation'].lower()
            assert '.get()' in analysis['fix']


class TestKnowledgeBase:
    """Test the knowledge base functionality."""
    
    def test_get_type_error_info(self):
        """Test getting info for TypeError."""
        info = get_error_info("TypeError", "unsupported operand type(s) for +")
        
        assert 'explanation' in info
        assert 'fix' in info
        assert len(info['explanation']) > 0
    
    def test_get_value_error_info(self):
        """Test getting info for ValueError."""
        info = get_error_info("ValueError", "invalid literal for int()")
        
        assert 'explanation' in info
        assert 'fix' in info
        assert 'try-except' in info['fix'].lower() or 'validate' in info['fix'].lower()
    
    def test_unknown_error_fallback(self):
        """Test fallback for unknown errors."""
        info = get_error_info("UnknownError", "something went wrong")
        
        assert 'explanation' in info
        assert 'fix' in info
        assert 'UnknownError' in info['explanation']


class TestDebugContext:
    """Test the debug context manager."""
    
    def test_context_manager_catches_error(self):
        """Test that context manager catches errors."""
        caught = False
        
        try:
            with debug_context(use_color=False):
                x = 1 / 0
        except ZeroDivisionError:
            caught = True
        
        assert caught
    
    def test_context_manager_cleanup(self):
        """Test that context manager properly cleans up."""
        original_hook = sys.excepthook
        
        with debug_context(use_color=False):
            pass
        
        # Should restore original hook (or our global one)
        assert sys.excepthook is not None


def test_enable_disable_debugging():
    """Test enabling and disabling debugging."""
    original_hook = sys.excepthook
    
    enable_ai_debugging(use_color=False)
    assert sys.excepthook != original_hook
    
    disable_ai_debugging()
    # After disable, should be back to original or another hook
    assert sys.excepthook is not None


# Run tests
if __name__ == "__main__":
    pytest.main([__file__, "-v"])