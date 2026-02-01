from typing import Tuple, List
from .generator import MazeGenerator
from .utils import Direction


def write_maze_file(
    generator: MazeGenerator,
    filepath: str,
    entry: Tuple[int, int],
    exit_pos: Tuple[int, int]
) -> None:
    """
    Write maze to output file in hexadecimal format.
    
    Args:
        generator: MazeGenerator instance with generated maze
        filepath: Path to output file
        entry: Entry coordinates (x, y)
        exit_pos: Exit coordinates (x, y)
        
    Raises:
        IOError: If file cannot be written
    """
    try:
        with open(filepath, 'w') as f:
            # Write maze grid (hex values)
            hex_string = generator.to_hex_string()
            f.write(hex_string)
            f.write('\n')
            
            # Empty line
            f.write('\n')
            
            # Entry coordinates
            f.write(f"{entry[0]},{entry[1]}\n")
            
            # Exit coordinates
            f.write(f"{exit_pos[0]},{exit_pos[1]}\n")
            
            # Shortest path
            path = generator.find_shortest_path(entry, exit_pos)
            path_string = generator.path_to_string(path)
            f.write(f"{path_string}\n")
            
    except IOError as e:
        raise IOError(f"Failed to write output file: {e}")