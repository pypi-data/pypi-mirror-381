"""
CursorFlow - AI-guided universal testing framework

Simple data collection engine that enables Cursor to autonomously test UI 
and iterate on designs with immediate visual feedback.

Declarative Actions | Batch Execution | Universal Log Collection | Visual Development
"""

from pathlib import Path

# Main API - clean and simple
from .core.cursorflow import CursorFlow

# Core components (for advanced usage)
from .core.browser_engine import BrowserEngine
from .core.log_monitor import LogMonitor
from .core.error_correlator import ErrorCorrelator

def _get_version():
    """Get version from git tag or fallback to default"""
    try:
        import subprocess
        result = subprocess.run(
            ['git', 'describe', '--tags', '--exact-match'],
            capture_output=True,
            text=True,
            cwd=Path(__file__).parent.parent
        )
        if result.returncode == 0:
            # Remove 'v' prefix if present
            return result.stdout.strip().lstrip('v')
    except Exception:
        pass
    
    try:
        # Try to get latest tag if not on exact tag
        result = subprocess.run(
            ['git', 'describe', '--tags', '--abbrev=0'],
            capture_output=True,
            text=True,
            cwd=Path(__file__).parent.parent
        )
        if result.returncode == 0:
            tag = result.stdout.strip().lstrip('v')
            # Add dev suffix if not on exact tag
            return f"{tag}-dev"
    except Exception:
        pass
    
    # Fallback version
    return "1.0.0-dev"

__version__ = _get_version()
__author__ = "GeekWarrior Development"

# Simple public API
__all__ = [
    "CursorFlow",        # Main interface for Cursor
    "BrowserEngine",     # Advanced browser control
    "LogMonitor",        # Advanced log monitoring
    "ErrorCorrelator",   # Advanced correlation analysis
    "check_for_updates", # Update checking
    "update_cursorflow", # Update management
]

# Update functions (for programmatic access)
def check_for_updates(project_dir: str = "."):
    """Check for CursorFlow updates"""
    import asyncio
    from .updater import check_updates
    return asyncio.run(check_updates(project_dir))

def update_cursorflow(project_dir: str = ".", force: bool = False):
    """Update CursorFlow package and rules"""
    import asyncio
    from .updater import update_cursorflow as _update
    return asyncio.run(_update(project_dir, force=force))
