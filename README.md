# A-Maze-ing

*This project has been created as part of the 42 curriculum by <your_login>.*

## Description

A Python maze generator that creates perfect mazes using the Recursive Backtracker 
algorithm. Features include:
- Configurable dimensions and entry/exit points
- Guaranteed single path between any two points (perfect maze)
- Hidden "42" pattern Easter egg
- Interactive ASCII terminal visualization
- Hexadecimal output format for data portability
- Reusable Python package

## Instructions

### Installation
\`\`\`bash
# Clone repository
git clone <your-repo-url>
cd a-maze-ing

# Install dependencies
make install
\`\`\`

### Running
\`\`\`bash
# Generate maze with default config
make run

# Or with custom config
python3 a_maze_ing.py my_config.txt
\`\`\`

### Configuration File Format

\`\`\`
# Required fields
WIDTH=20              # Maze width (5-200)
HEIGHT=15             # Maze height (5-200)
ENTRY=0,0             # Entry coordinates (x,y)
EXIT=19,14            # Exit coordinates (x,y)
OUTPUT_FILE=maze.txt  # Output file path
PERFECT=True          # Generate perfect maze (True/False)

# Optional fields
SEED=42               # Random seed for reproducibility
\`\`\`

## Algorithm

### Chosen Algorithm: Recursive Backtracker (DFS-based)

**Why this algorithm:**
- Guarantees perfect mazes (spanning tree property)
- Creates long, winding passages
- Easy to implement and understand
- Naturally handles the connectivity requirement
- Deterministic with seed support

**How it works:**
1. Start at a cell (entry point)
2. Mark current cell as visited
3. While there are unvisited neighbors:
   - Choose a random unvisited neighbor
   - Remove wall between current and chosen cell
   - Move to chosen cell (push to stack)
4. If no unvisited neighbors, backtrack (pop from stack)
5. Repeat until all cells visited

## Reusable Code

### Package Installation
\`\`\`bash
pip install dist/mazegen-1.0.0-py3-none-any.whl
\`\`\`

### Usage Example
\`\`\`python
from mazegen import MazeGenerator

# Create and generate maze
gen = MazeGenerator(width=20, height=15, seed=42)
gen.generate(entry=(0, 0), exit=(19, 14))

# Get maze data
hex_output = gen.to_hex_string()
path = gen.find_shortest_path((0, 0), (19, 14))
\`\`\`

See package documentation for full API reference.

## Team Management

### Team Members
- <your_login>: Lead developer, algorithm implementation, package creation

### Project Planning

**Initial Plan:**
- Day 1: Setup, config parser, basic generator
- Day 2: Pathfinding, output writer, visualizer
- Day 3: Package creation, testing, documentation

**Actual Timeline:**
- Completed in one focused session (tonight!)
- Used feature branches for organized development
- Regular commits and pushes for progress tracking

**What Worked Well:**
- Breaking project into clear milestones
- Git workflow with feature branches
- Frequent testing during development
- Clear separation of concerns (modules)

**Areas for Improvement:**
- Could add more comprehensive testing
- Visualizer could have more features
- Performance optimization for large mazes

### Tools Used
- Git for version control
- Make for automation
- pytest for testing (planned)
- mypy for type checking
- flake8 for linting

## Resources

### Classic References
- [Maze Generation Algorithms](http://weblog.jamisbuck.org/2011/2/7/maze-generation-algorithm-recap)
- [Think Labyrinth: Maze Algorithms](http://www.astrolog.org/labyrnth/algrithm.htm)
- [Wikipedia: Maze Generation](https://en.wikipedia.org/wiki/Maze_generation_algorithm)

### AI Usage
- Code structure suggestions and boilerplate
- Algorithm pseudocode review
- Documentation formatting help
- Debug assistance for wall encoding logic
- All AI-generated code was reviewed, understood, and tested before integration

## Features

### Implemented
- ✅ Recursive Backtracker maze generation
- ✅ Perfect maze guarantee (single path)
- ✅ Hexadecimal output format
- ✅ BFS pathfinding
- ✅ ASCII terminal visualization
- ✅ Interactive controls (path toggle, regenerate)
- ✅ "42" pattern Easter egg
- ✅ Python package distribution

### Future Enhancements
- Multiple algorithm support (Prim's, Kruskal's)
- MLX graphical renderer
- Animation during generation
- Color themes
- Larger maze support with optimization