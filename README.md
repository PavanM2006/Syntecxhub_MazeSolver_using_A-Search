A* Maze Solver — Progressive AI Search Visualization
An interactive Python implementation of the A* search algorithm that generates a 10×10 maze, intelligently searches for a path from start to goal, and visualizes the complete exploration process before animating the final path.

Overview
A* Maze Solver is an Artificial Intelligence project focused on demonstrating how the A* search algorithm works in a grid-based maze.

The project goes beyond simply finding a path. It captures the order in which A* explores cells and progressively visualizes that exploration inside the maze.

Once the goal is reached, the calculated path is highlighted and an agent animates the final route from the start position to the goal.

The implementation uses:
•	A* Search Algorithm
•	Manhattan Distance Heuristic
•	Python heapq Priority Queue
•	PyMaze 1.0.1
•	Tkinter-based visualization through PyMaze

Key Features
•	A* pathfinding on a dynamically generated maze
•	Manhattan-distance heuristic
•	Priority queue using Python's heapq
•	10×10 configurable maze
•	Maze generation with additional loops
•	Progressive visualization of explored cells
•	Start and goal markers
•	Final path visualization
•	Animated agent movement
•	Console logging of A* search decisions
•	g(n), h(n) and f(n) score tracking
•	Path length calculation
•	Number of explored cells
•	Execution-time measurement
•	No-path handling
•	Configurable animation speed

How the Application Works
The application follows a two-stage process. Stage 1 — A* Search
 
The algorithm explores the maze using:

f(n) = g(n) + h(n)

g(n)  cost from the start to the current cell
h(n)  estimated cost from the current cell to the goal f(n)  estimated total cost
The cell with the lowest f(n) value is prioritized. Stage 2 — Visualization
1.	The explored cells are revealed progressively.
2.	The final path is highlighted.
3.	The A* agent follows the calculated path.
4.	Footprints show the agent's movement.

A* Search
Heuristic

The project uses the Manhattan Distance heuristic:

h(n) = |x1 - x2| + |y1 - y2|

The heuristic is appropriate for the four-directional movement used by the maze. Search Strategy
The implementation maintains:

open_list Priority queue containing candidate cells closed_set Tracks cells that have already been expanded g_score Stores the current known cost from the start
came_from Stores parent relationships for path reconstruction exploration_order Records the exact order in which cells are explored

The priority queue is implemented using heapq. Each queued node contains:
(f_score, counter, cell)

The counter provides deterministic tie-breaking between nodes with equal priority.

Maze Generation
The maze is generated using PyMaze. Current configuration:
Rows : 10
 
Columns : 10
Start : (1, 1)
Goal : (10, 10)

The maze uses loopPercent=30 to introduce additional connections, allowing multiple possible routes between cells.

Visualization
The project separates the algorithmic search from the visual presentation.

Search Phase
During A* execution, every cell removed from the priority queue is recorded in exploration_order. This allows the project to reproduce the exact exploration sequence visually.

Progressive Exploration
The GUI reveals explored cells one at a time using the Tkinter event scheduler provided through PyMaze.

Final Path
After exploration is complete, the calculated A* path is highlighted and the agent follows it using PyMaze's path-tracing functionality.

Visualization Legend
Red Square  Start position Green Square  Goal position Blue Arrow  A* agent
Blue Marks  Explored cells Yellow Marks  Final A* path
White Footprints Agent movement trail

Visualization Flow
Generate Maze

Initialize A*

Calculate g(n), h(n), f(n)

Select Lowest f(n)

Explore Neighbours

Goal Found?
/	\
No	Yes
	
Continue	Reconstruct Path Search		
\	Progressive Visualization
\	
■■■ Animate Final A* Path

Path Reconstruction
 
When the goal is reached, the algorithm reconstructs the path using the came_from dictionary.

Goal

Parent

Parent

Start

The path is then reversed:

Start  Cell  Cell  ...  Goal

Console Output
During exploration:

Visiting: (row, column) | g = ... | h = ... | f = ... After the search, the program reports information such as:
Status	: SUCCESS
Algorithm	: A*
Start	: (1, 1)
Goal	: (10, 10)
Path length	: ...
Cells explored	: ...
Execution time	: ... sec
Heuristic	: Manhattan

If the goal cannot be reached, the program reports a NO PATH status.

Configuration

ROWS	10
COLS	10
START	(1, 1)
GOAL	(10, 10)
EXPLORATION_DELAY	180 ms
FINAL_PATH_DELAY	700 ms

These values can be modified in maze_test.py to change the maze dimensions, start/goal positions, and animation spe

Technology Stack
Python Core programming language A* AI search algorithm
PyMaze Maze generation and visualization heapq Priority queue
Tkinter Event Loop Progressive animation time Execution-time measurement
Requirements
•	Python 3.x
•	pyamaze==1.0.1
 
The exact dependency is specified in requirements.txt.

Installation
1.	Clone the repository

git clone https://github.com/PavanM2006/Syntecxhub_MazeSolver_using_A-Search.git

2.	Navigate to the project

cd Syntecxhub_MazeSolver_using_A-Search

3.	Install dependencies

pip install -r requirements.txt

Run the Project
python maze_test.py

The program will:
1.	Create the maze.
2.	Run the A* search.
3.	Print the exploration details.
4.	Display search statistics.
5.	Open the graphical maze.
6.	Animate the explored cells.
7.	Highlight the final path.
8.	Animate the A* agent along the solution.

Project Structure

Syntecxhub_MazeSolver_using_A-Search/
│
├── maze_test.py
│   └── A* implementation, maze generation,
│       search visualization and agent animation
│
├── requirements.txt
│   └── Python dependency configuration
│
├── README.md
│   └── Project documentation
│
└── .gitignore
    └── Git ignore configuration

Complexity
Let V be the number of cells and E the number of valid connections.

Time Complexity O(E log V)

Space Complexity O(V)

The algorithm stores the open list, closed set, score mappings, parent relationships, and exploration order.

Why A*?
 
A* combines actual path cost with estimated remaining cost:

Actual Cost + Estimated Remaining Cost = Search Priority For this project:
f(n) = g(n) + h(n)

with Manhattan Distance used for h(n).

This makes the search goal-directed while still accounting for the cost already travelled.

Project Highlights
•	Informed search
•	Heuristic-based decision making
•	Graph traversal
•	Priority queues
•	Path reconstruction
•	State-space exploration
•	Algorithm visualization
•	GUI event scheduling
•	Performance measurement

Future Improvements
■	Interactive maze generation
■	User-defined start and goal positions
■	Manual wall placement
■	Diagonal movement
■	Alternative heuristics
■	BFS vs DFS vs Dijkstra vs A* comparison
■	Real-time open/closed set statistics
■	Interactive animation controls
■	Command-line configuration
■	GIF/MP4 export
■	Improved visualization interface

Learning Outcomes
Artificial Intelligence
•	A* Search
•	Heuristic Search
•	Pathfinding
•	State-space exploration

Data Structures
•	Priority Queue
•	Heap
•	Set
•	Dictionary
 
Python
•	Functions
•	Tuples
•	Dictionaries
•	Sets
•	Lists
•	Modules
•	Performance measurement

Visualization
•	PyMaze
•	Tkinter event scheduling
•	Progressive animation
•	Agent path tracing


