"""ASCII terminal visualizer for mazes."""

from typing import Tuple, Optional, List
from .generator import MazeGenerator
from .utils import Direction, has_wall
from colorama import Fore, Style, init

class AsciiVisualizer:
	"""ASCII terminal maze visualizer."""
	
	def __init__(self, generator: MazeGenerator) -> None:
		"""Initialize visualizer."""
		self.generator = generator
		self.show_path = False
		self.path: Optional[List[Direction]] = None
		self.entry: Optional[Tuple[int, int]] = None
		self.exit: Optional[Tuple[int, int]] = None
	
	def set_path(
		self,
		entry: Tuple[int, int],
		exit_pos: Tuple[int, int]
	) -> None:
		"""Calculate and store path."""
		self.entry = entry
		self.exit = exit_pos
		self.path = self.generator.find_shortest_path(entry, exit_pos)
		self.wall_color = Fore.WHITE
		self.colors = [Fore.WHITE, Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.MAGENTA, Fore.CYAN]
		self.color_index = 0
	
	def cycle_color(self) -> None:
		"""Cycle through wall colors."""
		self.color_index = (self.color_index + 1) % len(self.colors)
		self.wall_color = self.colors[self.color_index]
	
	def render(self) -> str:
		"""
		Render maze as ASCII art.
		
		Returns:
			Multi-line string representation
		"""
		lines = []
		
		# Build path cells set for highlighting
		path_cells = set()
		if self.show_path and self.path and self.entry:
			current = self.entry
			path_cells.add(current)
			for direction in self.path:
				from .utils import get_neighbor
				current = get_neighbor(current, direction)
				path_cells.add(current)
		
		# Top border with color
		lines.append(self.wall_color + '+' + '---+' * self.generator.width + Style.RESET_ALL)
		
		# For each row
		for y in range(self.generator.height):
			# Cell line with vertical walls
			cell_line = ''
			for x in range(self.generator.width):
				cell = self.generator.get_cell(x, y)
				
				# West wall at start of row
				if x == 0:
					cell_line += self.wall_color + '|' + Style.RESET_ALL
				
				# Determine cell content
				if (x, y) == self.entry:
					content = Fore.GREEN + ' E ' + Style.RESET_ALL
				elif (x, y) == self.exit:
					content = Fore.RED + ' X ' + Style.RESET_ALL
				elif (x, y) in path_cells:
					content = Fore.YELLOW + ' * ' + Style.RESET_ALL
				else:
					content = '   '
				
				cell_line += content
				
				# East wall
				if has_wall(cell, Direction.EAST):
					cell_line += self.wall_color + '|' + Style.RESET_ALL
				else:
					cell_line += ' '
			
			lines.append(cell_line)
			
			# Horizontal walls line
			wall_line = ''
			for x in range(self.generator.width):
				cell = self.generator.get_cell(x, y)
				
				# Corner at start
				if x == 0:
					wall_line += self.wall_color + '+' + Style.RESET_ALL
				
				# South wall
				if has_wall(cell, Direction.SOUTH):
					wall_line += self.wall_color + '---+' + Style.RESET_ALL
				else:
					wall_line += '   ' + self.wall_color + '+' + Style.RESET_ALL
			
			lines.append(wall_line)
		
		return '\n'.join(lines)
	
	def toggle_path(self) -> None:
		"""Toggle path display."""
		self.show_path = not self.show_path


def display_interactive(
	generator: MazeGenerator,
	entry: Tuple[int, int],
	exit_pos: Tuple[int, int],
	config: dict
) -> None:
	"""
	Interactive terminal display with user controls.
	
	Args:
		generator: MazeGenerator instance
		entry: Entry coordinates
		exit_pos: Exit coordinates
		config: Configuration dictionary
	"""
	import os
	
	# Initialize colorama
	init()
	
	visualizer = AsciiVisualizer(generator)
	visualizer.set_path(entry, exit_pos)
	
	while True:
		# Clear screen
		os.system('clear' if os.name != 'nt' else 'cls')
		
		# Render maze
		print(visualizer.render())
		print()
		
		# Show controls
		print("Controls:")
		print("  [P] Toggle path")
		print("  [C] Cycle wall color")
		print("  [R] Regenerate maze")
		print("  [Q] Quit")
		print()
		
		# Get input
		choice = input("Command: ").strip().upper()
		
		if choice == 'Q':
			break
		elif choice == 'P':
			visualizer.toggle_path()
		elif choice == 'C':
			visualizer.cycle_color()
		elif choice == 'R':
			# Regenerate
			generator.generate(entry, exit_pos)
			visualizer.set_path(entry, exit_pos)
		else:
			print("Invalid command!")
			input("Press Enter to continue...")