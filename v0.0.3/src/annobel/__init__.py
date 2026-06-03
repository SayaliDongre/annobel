"""Top-level annobel namespace package."""
from .main import main, run  # noqa: F401

__all__ = ["main", "run"]
__version__ = "0.0.3"  # bumped from 0.0.2 to 0.0.3 adding empty label creation by default
