"""Maze generator package."""

from .config_parser import parse_config, ConfigParseError
from .generator import MazeGenerator
from .output_writer import write_maze_file

__all__ = ['parse_config', 'ConfigParseError', 'MazeGenerator', 'write_maze_file']
__version__ = "1.0.0"