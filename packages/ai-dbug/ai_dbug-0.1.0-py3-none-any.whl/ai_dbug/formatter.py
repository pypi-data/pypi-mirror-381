import sys
import os

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.syntax import Syntax
    from rich.text import Text
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False
    # Fallback to colorama
    try:
        from colorama import init, Fore, Style
        init(autoreset=True)
        COLORAMA_AVAILABLE = True
    except ImportError:
        COLORAMA_AVAILABLE = False


def is_windows_console():
    """Check if running in Windows console (not Windows Terminal)."""
    return sys.platform == 'win32' and 'WT_SESSION' not in os.environ


def safe_emoji(emoji, fallback):
    """Return emoji if supported, otherwise fallback character."""
    if is_windows_console():
        return fallback
    try:
        emoji.encode(sys.stdout.encoding or 'utf-8')
        return emoji
    except (UnicodeEncodeError, AttributeError):
        return fallback


class ErrorFormatter:
    """Formats error analysis for display."""
    
    def __init__(self, use_color=True):
        self.use_color = use_color and (RICH_AVAILABLE or COLORAMA_AVAILABLE)
        self.is_windows_console = is_windows_console()
        
        # Set up console with proper encoding handling
        if RICH_AVAILABLE:
            try:
                # Try to create console with force_terminal for IDEs
                self.console = Console(
                    force_terminal=True,
                    force_interactive=False,
                    legacy_windows=self.is_windows_console,
                    safe_box=self.is_windows_console,
                    highlight=False  # Disable highlighting that might have Unicode issues
                )
            except Exception:
                # Fallback to basic console
                self.console = Console(legacy_windows=True, safe_box=True)
    
    def format_error(self, analysis: dict) -> str:
        """
        Format error analysis for display.
        
        Args:
            analysis: Error analysis dictionary
            
        Returns:
            Formatted string
        """
        # Force flush to ensure output appears in IDEs
        try:
            sys.stdout.flush()
            sys.stderr.flush()
        except:
            pass
        
        if RICH_AVAILABLE and self.use_color:
            return self._format_with_rich(analysis)
        elif COLORAMA_AVAILABLE and self.use_color:
            return self._format_with_colorama(analysis)
        else:
            return self._format_plain(analysis)
    
    def _format_with_rich(self, analysis: dict):
        """Format using rich library."""
        console = self.console
        
        try:
            # Safe emoji characters
            bug = safe_emoji("🐛", "[!]")
            error_icon = safe_emoji("❌", "[X]")
            location_icon = safe_emoji("📍", "[@]")
            bulb_icon = safe_emoji("💡", "[?]")
            tool_icon = safe_emoji("🔧", "[+]")
            doc_icon = safe_emoji("📝", "[~]")
            
            # Header
            console.print("\n" + "="*70, style="bold red")
            console.print(f"{bug} AI-DBUG: Error Analysis", style="bold red", justify="center")
            console.print("="*70 + "\n", style="bold red")
            
            # Error type and message
            console.print(Panel(
                f"[bold red]{analysis['error_type']}[/bold red]\n{analysis['error_message']}",
                title=f"{error_icon} Error",
                border_style="red"
            ))
            
            # Location
            if analysis['error_location']:
                loc = analysis['error_location']
                console.print(Panel(
                    f"[cyan]File:[/cyan] {loc['file']}\n"
                    f"[cyan]Line:[/cyan] {loc['line']}\n"
                    f"[cyan]Function:[/cyan] {loc['function']}\n"
                    f"[yellow]Code:[/yellow] {loc['code']}",
                    title=f"{location_icon} Location",
                    border_style="cyan"
                ))
            
            # Explanation
            console.print(Panel(
                analysis['explanation'],
                title=f"{bulb_icon} What Happened?",
                border_style="yellow"
            ))
            
            # Fix suggestion
            console.print(Panel(
                analysis['fix'],
                title=f"{tool_icon} How to Fix",
                border_style="green"
            ))
            
            # Example
            if analysis.get('example'):
                try:
                    syntax = Syntax(
                        analysis['example'],
                        "python",
                        theme="monokai",
                        line_numbers=True,
                        word_wrap=True
                    )
                    console.print(Panel(
                        syntax,
                        title=f"{doc_icon} Example",
                        border_style="blue"
                    ))
                except Exception:
                    # Fallback to plain text if syntax highlighting fails
                    console.print(Panel(
                        analysis['example'],
                        title=f"{doc_icon} Example",
                        border_style="blue"
                    ))
            
            console.print()
        except UnicodeEncodeError:
            # If rich fails due to encoding, fallback to plain text
            return self._format_plain(analysis)
        except Exception as e:
            # Any other error, fallback to plain text
            print(f"\n[AI-DBUG formatting error, using plain text: {e}]\n")
            return self._format_plain(analysis)
        
        return ""  # Rich prints directly
    
    def _format_with_colorama(self, analysis: dict) -> str:
        """Format using colorama library."""
        output = []
        
        try:
            # Safe emoji characters
            bug = safe_emoji("🐛", "[!]")
            error_icon = safe_emoji("❌", "[X]")
            location_icon = safe_emoji("📍", "[@]")
            bulb_icon = safe_emoji("💡", "[?]")
            tool_icon = safe_emoji("🔧", "[+]")
            doc_icon = safe_emoji("📝", "[~]")
            
            # Header
            output.append(f"\n{Fore.RED}{'='*70}")
            output.append(f"{Fore.RED}{Style.BRIGHT}{bug} AI-DBUG: Error Analysis")
            output.append(f"{Fore.RED}{'='*70}\n")
            
            # Error
            output.append(f"{Fore.RED}{Style.BRIGHT}{error_icon} ERROR")
            output.append(f"{Fore.RED}{analysis['error_type']}: {analysis['error_message']}\n")
            
            # Location
            if analysis['error_location']:
                loc = analysis['error_location']
                output.append(f"{Fore.CYAN}{Style.BRIGHT}{location_icon} LOCATION")
                output.append(f"{Fore.CYAN}File: {loc['file']}")
                output.append(f"{Fore.CYAN}Line: {loc['line']}")
                output.append(f"{Fore.CYAN}Function: {loc['function']}")
                output.append(f"{Fore.YELLOW}Code: {loc['code']}\n")
            
            # Explanation
            output.append(f"{Fore.YELLOW}{Style.BRIGHT}{bulb_icon} WHAT HAPPENED?")
            output.append(f"{Fore.WHITE}{analysis['explanation']}\n")
            
            # Fix
            output.append(f"{Fore.GREEN}{Style.BRIGHT}{tool_icon} HOW TO FIX")
            output.append(f"{Fore.WHITE}{analysis['fix']}\n")
            
            # Example
            if analysis.get('example'):
                output.append(f"{Fore.BLUE}{Style.BRIGHT}{doc_icon} EXAMPLE")
                output.append(f"{Fore.WHITE}{analysis['example']}\n")
            
            result = "\n".join(output)
            print(result)
        except UnicodeEncodeError:
            return self._format_plain(analysis)
        
        return ""
    
    def _format_plain(self, analysis: dict) -> str:
        """Format without colors - pure ASCII."""
        output = []
        
        output.append("\n" + "="*70)
        output.append("AI-DBUG: Error Analysis")
        output.append("="*70 + "\n")
        
        output.append("ERROR")
        output.append(f"{analysis['error_type']}: {analysis['error_message']}\n")
        
        if analysis['error_location']:
            loc = analysis['error_location']
            output.append("LOCATION")
            output.append(f"File: {loc['file']}")
            output.append(f"Line: {loc['line']}")
            output.append(f"Function: {loc['function']}")
            output.append(f"Code: {loc['code']}\n")
        
        output.append("WHAT HAPPENED?")
        output.append(f"{analysis['explanation']}\n")
        
        output.append("HOW TO FIX")
        output.append(f"{analysis['fix']}\n")
        
        if analysis.get('example'):
            output.append("EXAMPLE")
            output.append(f"{analysis['example']}\n")
        
        result = "\n".join(output)
        print(result)
        return result
