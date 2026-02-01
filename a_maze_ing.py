#!/usr/bin/env python3
"""
A-Maze-ing: Maze generator and visualizer.

Usage: python3 a_maze_ing.py <config_file>
"""

import sys
from src.mazegen.visualizer import display_interactive
from src.mazegen import (
	parse_config,
	ConfigParseError,
	MazeGenerator,
	write_maze_file
)


def main() -> None:
	"""Main entry point."""
	# Check arguments
	if len(sys.argv) != 2:
		print("Usage: python3 a_maze_ing.py <config_file>", file=sys.stderr)
		sys.exit(1)
	
	config_file = sys.argv[1]
	
	try:
		# Parse configuration
		print(f"Loading configuration from {config_file}...")
		config = parse_config(config_file)
		
		# Create generator
		print(f"Generating {config['WIDTH']}x{config['HEIGHT']} maze...")
		generator = MazeGenerator(
			width=config['WIDTH'],
			height=config['HEIGHT'],
			seed=config.get('SEED')
		)
		
		# Generate maze
		generator.generate(config['ENTRY'], config['EXIT'])
		
		# Write output file
		output_file = config['OUTPUT_FILE']
		print(f"Writing maze to {output_file}...")
		write_maze_file(
			generator,
			output_file,
			config['ENTRY'],
			config['EXIT']
		)
		
		print(f"✓ Maze generated successfully!")
		print(f"  Entry: {config['ENTRY']}")
		print(f"  Exit: {config['EXIT']}")
		print(f"  Output: {output_file}")
		
		# TODO: Launch visualizer
		print("\nLaunching visualizer...")
		display_interactive(generator, config['ENTRY'], config['EXIT'], config)
		
	except FileNotFoundError as e:
		print(f"Error: {e}", file=sys.stderr)
		sys.exit(1)
	except ConfigParseError as e:
		print(f"Configuration error: {e}", file=sys.stderr)
		sys.exit(1)
	except Exception as e:
		print(f"Unexpected error: {e}", file=sys.stderr)
		sys.exit(1)


if __name__ == "__main__":
	main()