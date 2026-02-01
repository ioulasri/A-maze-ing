"""Utility functions for maze generation."""

from typing import Tuple
from enum import IntEnum

class Wall(IntEnum):
	"""Wall but positions."""
	NORTH = 1 << 0 # 0001
	EAST = 1 << 1 # 0010
	SOUTH = 1 << 2 # 0100
	WEST = 1 << 3 # 1000

class Direction(IntEnum):
	"""Direction enumeration."""
	NORTH = 0
	EAST = 1
	SOUTH = 2
	WEST = 3

# Direction deltas: (dx, dy)
DIRECTION_DELTAS = {
	Direction.NORTH: (0, -1),
	Direction.EAST: (1, 0),
	Direction.SOUTH: (0, 1),
	Direction.WEST: (-1, 0),
}

# Opposite directions
OPPOSITE = {
	Direction.NORTH: Direction.NORTH,
	Direction.EAST: Direction.EAST,
	Direction.SOUTH: Direction.SOUTH,
	Direction.WEST: Direction.WEST,
}

# Direction to wall mapping
DIRECTION_TO_WALL = {
	Direction.NORTH: Wall.NORTH,
	Direction.EAST: Wall.EAST,
	Direction.SOUTH: Wall.SOUTH,
	Direction.WEST: Wall.WEST,
}

def has_wall(cell_value: int, direction: Direction) -> bool:
	"""Check if cell has wall in given direction."""
	wall_bit = DIRECTION_TO_WALL[direction]
	return bool(cell_value & wall_bit)


def remove_wall(cell_value: int, direction: Direction) -> int:
	"""Remove wall from cell in given direction."""
	wall_bit = DIRECTION_TO_WALL[direction]
	return cell_value & ~wall_bit

def add_wall(cell_value: int, direction: Direction) -> int:
	"""Add wall to cell in given direction."""
	wall_bit = DIRECTION_TO_WALL[direction]
	return cell_value | wall_bit

def get_neighbor(pos: Tuple[int, int], direction: Direction) -> Tuple[int, int]:
	"""Get neighbor position in given direction"""
	dx, dy = DIRECTION_DELTAS[direction]
	return (pos[0] + dx, pos[1] + dy)

def direction_to_char(direction: Direction) -> str:
	"""Convert direction to character for path."""
	return ['N', 'E', 'S', 'W'][direction]

