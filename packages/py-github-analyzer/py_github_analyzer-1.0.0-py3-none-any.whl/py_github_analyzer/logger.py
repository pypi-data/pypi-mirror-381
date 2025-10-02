import os
import sys
from typing import Optional, Dict, Any, Union

from rich.console import Console
from rich.logging import RichHandler
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeRemainingColumn
from rich.panel import Panel
import logging

# Windows UTF-8 environment setup
if os.name == 'nt':  # Windows
    os.environ['PYTHONIOENCODING'] = 'utf-8'
    os.environ['PYTHONLEGACYWINDOWSFSENCODING'] = '0'

# Force console to UTF-8 encoding
try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')
except AttributeError:
    # reconfigure method doesn't exist in Python < 3.7
    pass
except Exception:
    # Ignore other errors and continue
    pass


class AnalyzerLogger:
    """Enhanced logger with Rich formatting and progress tracking"""

    def __init__(self, verbose: bool = False):
        self.verbose = verbose

        # Windows compatible Console settings
        console_kwargs = {
            'width': 100,
            'force_terminal': True,
            'no_color': False,
            'tab_size': 4,
            'stderr': False  # Use stdout
        }

        # Windows encoding issue resolution
        if os.name == 'nt':  # Windows
            console_kwargs.update({
                'legacy_windows': False,  # Support new Windows Terminal
                'force_terminal': True,
                'encoding': 'utf-8'
            })

        try:
            self.console = Console(**console_kwargs)
        except Exception as e:
            # Fallback console setup
            try:
                self.console = Console(force_terminal=True, no_color=True, stderr=False)
            except Exception:
                # Last resort: basic console
                self.console = Console()

        self.setup_logging()

        # Progress tracking
        self.progress = None
        self.current_task = None

        # Emoji mapping for Windows compatibility
        self.emoji_map = {
            'info': '🔍' if self._supports_unicode() else 'i',
            'success': '✅' if self._supports_unicode() else '+',
            'warning': '⚠️' if self._supports_unicode() else '!',
            'error': '❌' if self._supports_unicode() else 'x',
            'debug': '🐛' if self._supports_unicode() else 'd',
            'progress': '⏳' if self._supports_unicode() else '.',
            'download': '📥' if self._supports_unicode() else '>',
            'upload': '📤' if self._supports_unicode() else '<',
            'file': '📁' if self._supports_unicode() else 'f',
            'code': '💻' if self._supports_unicode() else 'c'
        }

    def _supports_unicode(self) -> bool:
        """Check if terminal supports Unicode characters"""
        try:
            # Check UTF-8 support on Windows
            if os.name == 'nt':
                # Windows 10 1903+ has good UTF-8 support
                return True
            # Most Unix systems support UTF-8
            return sys.stdout.encoding.lower() in ['utf-8', 'utf8']
        except:
            return False

    def setup_logging(self):
        """Setup Rich logging handler"""
        try:
            # Rich handler configuration
            rich_handler = RichHandler(
                console=self.console,
                show_path=self.verbose,
                show_time=True,
                rich_tracebacks=True,
                tracebacks_show_locals=self.verbose,
                markup=True,
                omit_repeated_times=False
            )

            # Logger configuration
            logging.basicConfig(
                level=logging.DEBUG if self.verbose else logging.WARNING,
                format="%(message)s",
                datefmt="[%X]",
                handlers=[rich_handler],
                force=True
            )

            self.logger = logging.getLogger("github-analyzer")

        except Exception as e:
            # Fallback to basic logging if Rich fails
            logging.basicConfig(
                level=logging.DEBUG if self.verbose else logging.WARNING,
                format='%(asctime)s - %(levelname)s - %(message)s',
                force=True
            )

            self.logger = logging.getLogger("github-analyzer")
            print(f"Warning: Rich logging failed, using basic logging: {e}")

    def _safe_string(self, text: Union[str, Any]) -> str:
        """Convert string to safe encoding"""
        if not isinstance(text, str):
            text = str(text)

        try:
            # Safe string conversion on Windows
            if os.name == 'nt':
                # Handle Unicode characters safely
                return text.encode('utf-8', errors='replace').decode('utf-8')
            else:
                return text
        except Exception:
            # Last resort: convert to ASCII
            return text.encode('ascii', errors='replace').decode('ascii')

    def _safe_print(self, message: str, style: Optional[str] = None, emoji: str = ''):
        """Safely print message with fallback"""
        try:
            safe_message = self._safe_string(message)
            if emoji:
                full_message = f"{emoji} {safe_message}"
            else:
                full_message = safe_message

            if style:
                self.console.print(full_message, style=style)
            else:
                self.console.print(full_message)

        except UnicodeEncodeError:
            # Fallback: ASCII only
            safe_message = self._safe_string(message)
            fallback_emoji = emoji.encode('ascii', errors='ignore').decode('ascii')
            fallback_message = f"{fallback_emoji} {safe_message}" if fallback_emoji else safe_message

            try:
                if style:
                    self.console.print(fallback_message, style=style)
                else:
                    self.console.print(fallback_message)
            except:
                # Last resort: basic print
                print(fallback_message)

        except Exception as e:
            # Complete fallback
            safe_message = self._safe_string(message)
            print(f"{safe_message}")

    def info(self, message: str):
        """Log info message"""
        emoji = self.emoji_map['info']
        self._safe_print(message, style="cyan", emoji=emoji)

    def success(self, message: str):
        """Log success message"""
        emoji = self.emoji_map['success']
        self._safe_print(message, style="green", emoji=emoji)

    def warning(self, message: str):
        """Log warning message"""
        emoji = self.emoji_map['warning']
        self._safe_print(message, style="yellow", emoji=emoji)
        safe_message = self._safe_string(message)
        self.logger.warning(safe_message)

    def error(self, message: str):
        """Log error message"""
        emoji = self.emoji_map['error']
        self._safe_print(message, style="red", emoji=emoji)
        safe_message = self._safe_string(message)
        self.logger.error(safe_message)

    def debug(self, message: str):
        """Log debug message"""
        if self.verbose:
            emoji = self.emoji_map['debug']
            safe_message = self._safe_string(message)
            self.logger.debug(f"{emoji} {safe_message}")

    def progress_start(self, description: str) -> Progress:
        """Start progress tracking"""
        try:
            self.progress = Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
                TimeRemainingColumn(),
                console=self.console
            )

            self.progress.start()
            self.current_task = self.progress.add_task(self._safe_string(description), total=None)
            return self.progress

        except Exception as e:
            self.debug(f"Progress start failed: {e}")
            return None

    def progress_update(self, advance: int = 1, description: Optional[str] = None):
        """Update progress"""
        if self.progress and self.current_task is not None:
            try:
                update_kwargs = {}
                if advance:
                    update_kwargs['advance'] = advance
                if description:
                    update_kwargs['description'] = self._safe_string(description)

                self.progress.update(self.current_task, **update_kwargs)

            except Exception as e:
                self.debug(f"Progress update failed: {e}")

    def progress_finish(self):
        """Finish progress tracking"""
        if self.progress:
            try:
                self.progress.stop()
                self.progress = None
                self.current_task = None
            except Exception as e:
                self.debug(f"Progress finish failed: {e}")

    def print_summary_table(self, data: Dict[str, str], title: str = "Analysis Summary"):
        """Print formatted summary table"""
        try:
            table = Table(
                title=self._safe_string(title),
                show_header=True,
                header_style="bold magenta",
                title_style="bold blue"
            )

            table.add_column("Metric", style="cyan", width=22)
            table.add_column("Value", style="green", width=18)

            for key, value in data.items():
                safe_key = self._safe_string(key)
                safe_value = self._safe_string(value)
                table.add_row(safe_key, safe_value)

            self.console.print(table)

        except Exception as e:
            # Fallback to simple print
            self.debug(f"Table print failed: {e}")
            safe_title = self._safe_string(title)
            print(f"\n{safe_title}:")
            print("-" * len(safe_title))
            for key, value in data.items():
                safe_key = self._safe_string(key)
                safe_value = self._safe_string(value)
                print(f"  {safe_key}: {safe_value}")
            print()

    def print_file_list(self, files: list, title: str = "Processed Files"):
        """Print formatted file list"""
        try:
            if not files:
                self.info("No files to display")
                return

            table = Table(
                title=self._safe_string(title),
                show_header=True,
                header_style="bold magenta"
            )

            table.add_column("Path", style="cyan", width=50)
            table.add_column("Size", style="green", width=10)
            table.add_column("Priority", style="yellow", width=8)

            for file_info in files[:20]:  # Show only first 20 files
                if isinstance(file_info, dict):
                    path = self._safe_string(file_info.get('path', 'Unknown'))
                    size = file_info.get('size', 0)
                    priority = file_info.get('priority', 0)

                    # Format size
                    if size < 1024:
                        size_str = f"{size}B"
                    elif size < 1024 * 1024:
                        size_str = f"{size/1024:.1f}KB"
                    else:
                        size_str = f"{size/(1024*1024):.1f}MB"

                    table.add_row(path, size_str, str(priority))

            if len(files) > 20:
                table.add_row("...", "...", "...")
                table.add_row(f"({len(files)-20} more files)", "", "")

            self.console.print(table)

        except Exception as e:
            # Fallback to simple print
            self.debug(f"File list print failed: {e}")
            safe_title = self._safe_string(title)
            print(f"\n{safe_title}:")
            for i, file_info in enumerate(files[:10]):
                if isinstance(file_info, dict):
                    path = self._safe_string(file_info.get('path', 'Unknown'))
                    size = file_info.get('size', 0)
                    print(f"  {i+1:2d}. {path} ({size} bytes)")
            if len(files) > 10:
                print(f"  ... and {len(files)-10} more files")

    def print_panel(self, content: str, title: str = "", style: str = "blue"):
        """Print content in a panel"""
        try:
            safe_content = self._safe_string(content)
            safe_title = self._safe_string(title)

            panel = Panel(
                safe_content,
                title=safe_title if title else None,
                border_style=style,
                padding=(1, 2)
            )

            self.console.print(panel)

        except Exception as e:
            # Fallback
            self.debug(f"Panel print failed: {e}")
            safe_content = self._safe_string(content)
            safe_title = self._safe_string(title)

            if title:
                print(f"\n=== {safe_title} ===")
            print(safe_content)
            if title:
                print("=" * (len(safe_title) + 8))

    def print_status(self, message: str, status: str = "info"):
        """Print status message with appropriate emoji"""
        emoji_key = status if status in self.emoji_map else 'info'
        emoji = self.emoji_map[emoji_key]

        style_map = {
            'info': 'cyan',
            'success': 'green',
            'warning': 'yellow',
            'error': 'red',
            'debug': 'dim'
        }

        style = style_map.get(status, 'white')
        self._safe_print(message, style=style, emoji=emoji)


# Global logger instance
_global_logger: Optional[AnalyzerLogger] = None
_verbose_mode: bool = False


def set_verbose(verbose: bool = True):
    """Set global verbose mode"""
    global _verbose_mode
    _verbose_mode = verbose


def get_logger(verbose: Optional[bool] = None) -> AnalyzerLogger:
    """Get or create global logger instance"""
    global _global_logger, _verbose_mode

    if verbose is None:
        verbose = _verbose_mode

    if _global_logger is None or _global_logger.verbose != verbose:
        _global_logger = AnalyzerLogger(verbose=verbose)

    return _global_logger


def setup_file_logging(log_file: str, level: int = logging.INFO):
    """Setup additional file logging"""
    try:
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(level)

        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        file_handler.setFormatter(formatter)
        logger = logging.getLogger("github-analyzer")
        logger.addHandler(file_handler)

        return True

    except Exception as e:
        print(f"Failed to setup file logging: {e}")
        return False


def log_system_info():
    """Log system information for debugging"""
    logger = get_logger()

    try:
        import platform
        import sys

        system_info = {
            "Platform": platform.platform(),
            "Python Version": sys.version.split()[0],
            "Encoding": sys.stdout.encoding if hasattr(sys.stdout, 'encoding') else 'unknown',
            "Terminal": os.environ.get('TERM', 'unknown'),
            "Console Width": str(logger.console.size.width if hasattr(logger.console, 'size') else 'unknown')
        }

        logger.print_summary_table(system_info, "System Information")

    except Exception as e:
        logger.debug(f"Failed to log system info: {e}")


# Convenience functions for direct use
def info(message: str):
    """Log info message"""
    get_logger().info(message)


def success(message: str):
    """Log success message"""
    get_logger().success(message)


def warning(message: str):
    """Log warning message"""
    get_logger().warning(message)


def error(message: str):
    """Log error message"""
    get_logger().error(message)


def debug(message: str):
    """Log debug message"""
    get_logger().debug(message)
