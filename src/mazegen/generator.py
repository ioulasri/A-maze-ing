from typing import List, Tuple, Optional, Set
import random
from .utils import (
	Direction, OPPOSITE, get_neighbor, remove_wall,
	direction_to_char, has_wall
)

class MazeGenerator:
	"""
	Generates random mazes using Recursive Backtracker algorithm.
	
	Attributes:
		width: Number of cells horizontally
		height: Numbers of cells vertically
		grid: 2D list of cell values (wall encoding)
		seed: Random seed for reproducibility
	"""
	def __init__(self, width: int, height: int, seed: Optional[int] = None):
		self.width = width
		self.height = height
		self.seed = seed

		if seed is not None:
			random.seed(seed)

		#Initialize grid: all walls closed (0xF = 15)
		self.grid: List[List[int]] = [
			[0xF for _ in range(width)]
			for _ in range(height)
		]
	
	def generate(self, entry: Tuple[int, int], exit_pos: Tuple[int, int]) -> None:
		# Use recursive backtracker starting from entry
		self._recursive_backtracker(entry)

		# TODO: add "42" Pattern
		# TODO: ensure no 3x3 open areas
		# TODO: add border walls where needed

	def _recursive_backtracker(self, start: Tuple[int, int]) -> None:
		stack = [start]
		visited: Set[Tuple[int, int]] = {start}

		while stack:
			current = stack[-1]

			# Get unvisited neighbors
			unvisited = self._get_unvisited_neighbors(current, visited)

			if unvisited:
				# Choose random neighbor
				next_cell = random.choice(unvisited)

				# Remove wall between current and next
				self._remove_wall_between(current, next_cell)

				# Mark as visited and add to stack
				visited.add(next_cell)
				stack.append(next_cell)

			else:
				# Backtrack
				stack.pop()

	def _get_unvisited_neighbors(self, pos: Tuple[int, int], visited: Set[Tuple[int, int]]) -> List[Tuple[int, int]]:
		"""Get list of valid unvisited neighbors"""

		neighbors = []

		for direction in Direction:
			neighbor = get_neighbor(pos, direction)

			# Check in neihbor is in bounds and unvisited
			if self._in_bounds(neighbor) and neighbor not in visited:
				neighbors.append(neighbor)

		return neighbors
	
	def _in_bounds(self, pos: Tuple[int, int]) -> bool:
		"""Check if position is within maze bounds."""
		x, y = pos
		return 0 <= x < self.width and 0 <= y < self.height
	
	def _remove_wall_between(self, pos1: Tuple[int, int], pos2: Tuple[int, int]) -> None:
		"""
		Remove wall between two adjacent cells.

		Maintaining consistency: both cells must agree on wall state
		"""
		# Find direction from pos1 to pos2
		dx = pos2[0] - pos1[0]
		dy = pos2[1] - pos1[1]

		if dx == 1:
			direction = Direction.EAST
		elif dx == -1:
			direction = Direction.WEST
		elif dy == 1:
			direction = Direction.SOUTH
		elif dy == -1:
			direction = Direction.NORTH
		else:
			raise ValueError("Cells are not adjacent")
		
		# Remove walls
		x1, y1 = pos1
		x2, y2 = pos2

		self.grid[y1][x1] = remove_wall(self.grid[y1][x1], direction)
		self.grid[y2][x2] = remove_wall(self.grid[y2][x2], OPPOSITE[direction])	

	def get_cell(self, x: int, y: int) -> int:
		"""Get cell value at position."""
		return self.grid[x][y]
	
	def to_hex_string(self) -> str:
		"""
		Convert maze to hexadecimal string format.
		
		Returns:
			Multi-line string with hex values
		"""

		lines = []
		for row in self.grid:
			line = ''.join(f"{cell:X}" for cell in row)
			lines.append(line)
		return '\n'.join(lines)
	
	