__version__ = "0.1.0"
__author__ = "AI-DBUG Contributors"
__license__ = "MIT"

from .core import enable_ai_debugging, disable_ai_debugging, AIDebugger, debug_context
from .analyzer import ErrorAnalyzer
from .formatter import ErrorFormatter

__all__ = [
    "enable_ai_debugging",
    "disable_ai_debugging",
    "AIDebugger", 
    "debug_context",
    "ErrorAnalyzer",
    "ErrorFormatter",
]
