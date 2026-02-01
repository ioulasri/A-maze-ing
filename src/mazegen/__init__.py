"""Maze generator package."""

from .config_parser import parse_config, ConfigParseError
from .generator import MazeGenerator

__version__ = "1.0.0"
__all__ = ['parse_config', 'ConfigParseError', 'MazeGenerator']