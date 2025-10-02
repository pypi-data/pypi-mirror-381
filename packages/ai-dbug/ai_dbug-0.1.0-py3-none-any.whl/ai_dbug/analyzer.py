import traceback
import sys
import io
from typing import Dict, List, Optional
from .knowledge_base import get_error_info


class ErrorAnalyzer:
    """Analyzes Python exceptions and provides detailed information."""
    
    def __init__(self):
        self.last_error = None
        self._setup_output_capture()
    
    def _setup_output_capture(self):
        """Setup to ensure output works in all environments (terminal, IDE, Jupyter)."""
        # Force stdout/stderr to be unbuffered for IDE compatibility
        if hasattr(sys.stdout, 'reconfigure'):
            try:
                sys.stdout.reconfigure(line_buffering=True)
                sys.stderr.reconfigure(line_buffering=True)
            except:
                pass
    
    def analyze_exception(self, exc_type, exc_value, exc_traceback) -> Dict:
        """
        Analyze an exception and extract relevant information.
        
        Args:
            exc_type: Exception class
            exc_value: Exception instance
            exc_traceback: Traceback object
            
        Returns:
            Dictionary containing error analysis
        """
        # Extract basic info
        error_type = exc_type.__name__ if exc_type else "Unknown"
        error_message = str(exc_value) if exc_value else ""
        
        # Extract traceback information
        tb_lines = traceback.extract_tb(exc_traceback)
        stack_trace = []
        
        for frame in tb_lines:
            stack_trace.append({
                "file": frame.filename,
                "line": frame.lineno,
                "function": frame.name,
                "code": frame.line
            })
        
        # Get the location where error occurred (last frame)
        error_location = stack_trace[-1] if stack_trace else None
        
        # Get AI explanation and fix
        error_info = get_error_info(error_type, error_message)
        
        # Build analysis result
        analysis = {
            "error_type": error_type,
            "error_message": error_message,
            "error_location": error_location,
            "stack_trace": stack_trace,
            "explanation": error_info["explanation"],
            "fix": error_info["fix"],
            "example": error_info.get("example", ""),
            "full_traceback": "".join(traceback.format_exception(exc_type, exc_value, exc_traceback))
        }
        
        self.last_error = analysis
        return analysis
    
    def get_relevant_code(self, filename: str, line_number: int, context: int = 3) -> List[str]:
        """
        Get code context around the error line.
        
        Args:
            filename: Path to the file
            line_number: Line number where error occurred
            context: Number of lines to show before and after
            
        Returns:
            List of code lines with context
        """
        try:
            with open(filename, 'r') as f:
                lines = f.readlines()
            
            start = max(0, line_number - context - 1)
            end = min(len(lines), line_number + context)
            
            return lines[start:end]
        except:
            return []
