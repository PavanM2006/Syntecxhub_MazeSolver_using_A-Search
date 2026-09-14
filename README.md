# A* Maze Solver — Progressive AI Search Visualization

> An interactive Python implementation of the A* search algorithm that generates a 10×10 maze, searches for a path from start to goal, and progressively visualizes the exploration process before animating the final path.

---

## 📌 Overview

**A* Maze Solver** is an Artificial Intelligence project that demonstrates how the **A* (A-Star) search algorithm** can be used to find an optimal path through a maze.

The project is designed not only to find the final path, but also to make the internal search process easier to understand.

During execution, the program:

1. Generates a maze.
2. Defines a start and goal position.
3. Calculates A* scores for candidate cells.
4. Selects the most promising cell.
5. Explores neighbouring cells.
6. Records the exploration sequence.
7. Reconstructs the final path.
8. Progressively visualizes the explored cells.
9. Animates the agent along the final path.
10. Displays search statistics in the console.

---

## 🚀 Key Features

- A* pathfinding algorithm
- Manhattan Distance heuristic
- Priority queue using Python `heapq`
- Dynamically generated maze
- 10 × 10 maze configuration
- Additional maze loops
- Progressive exploration visualization
- Start and goal indicators
- Final path visualization
- Animated agent movement
- Console-based search information
- `g(n)`, `h(n)`, and `f(n)` score tracking
- Path-length calculation
- Explored-cell count
- Execution-time measurement
- No-path handling
- Configurable animation speed

---

## 🧠 A* Search Algorithm

A* is an informed search algorithm that combines the actual cost of reaching a cell with an estimated cost of reaching the goal.

The evaluation function is:

```text
f(n) = g(n) + h(n)

Where:
g(n) = actual cost from the start node to the current node
h(n) = estimated cost from the current node to the goal
f(n) = estimated total cost of the path through the current node
The algorithm prioritizes the cell with the lowest f(n) value.
📐 Manhattan Distance Heuristic
This project uses Manhattan Distance as the heuristic.
The formula is:
h(n) = |x1 - x2| + |y1 - y2|
Where:
(x1, y1) = current cell
(x2, y2) = goal cell
Example
Current = (2, 3)
Goal    = (10, 10)

h(n) = |2 - 10| + |3 - 10|

     = 8 + 7

     = 15
Manhattan Distance is suitable for grid-based movement where movement is restricted to horizontal and vertical directions.
🔄 How A* Works in This Project
The search process can be summarized as:
Start
  │
  ▼
Calculate g(n)
  │
  ▼
Calculate h(n)
  │
  ▼
Calculate f(n) = g(n) + h(n)
  │
  ▼
Select cell with lowest f(n)
  │
  ▼
Explore neighbouring cells
  │
  ▼
Update scores and parent information
  │
  ▼
Is the goal reached?
  │
 ┌┴──────────────┐
 │               │
No              Yes
 │               │
 ▼               ▼
Continue      Reconstruct
search           path
                  │
                  ▼
            Display solution
🗺️ Maze Generation
The project uses the PyMaze library for maze generation and visualization.
Current Configuration
Parameter
Value
Maze Rows
10
Maze Columns
10
Start Position
(1, 1)
Goal Position
(10, 10)
Loop Percentage
30
The maze is generated with additional loops using a loop percentage of 30, providing multiple possible routes through the maze.
🔍 Search Strategy
The implementation uses several data structures to manage the A* search.
Data Structure
Purpose
open_list
Priority queue containing cells that can be explored
closed_set
Stores cells that have already been processed
g_score
Stores the current known cost from the start
came_from
Stores parent relationships for path reconstruction
exploration_order
Stores the order in which cells are explored
The priority queue is implemented using Python's built-in:
heapq
This allows the algorithm to efficiently select the most promising candidate cell.
🎨 Visualization
One of the main goals of this project is to make the A* search process visually understandable.
Instead of immediately displaying only the final solution, the application progressively displays the cells explored by the algorithm.
Search Visualization
During the search, the exploration order is stored in:
exploration_order
The recorded cells are then displayed sequentially.
A* Search
    │
    ▼
Exploration Order
    │
    ├── Cell 1
    ├── Cell 2
    ├── Cell 3
    ├── Cell 4
    ├── Cell 5
    ├── ...
    └── Goal
This allows the user to observe how A* searches through the maze before the final path is shown.
🛣️ Final Path
Once the goal is reached, the algorithm reconstructs the path using the came_from mapping.
The path is initially reconstructed backwards:
Goal
 │
 ▼
Parent
 │
 ▼
Parent
 │
 ▼
Start
It is then reversed:
Start → Cell → Cell → Cell → ... → Goal
The resulting path becomes the final solution.
🎨 Visualization Legend
Visual Element
Meaning
🔴 Red
Start position
🟢 Green
Goal position
🔵 Blue Arrow
A* agent
🔵 Blue Marks
Explored cells

📊 Console Output
The program provides information about the search process in the terminal.
During exploration, cells are displayed together with their A* scores.
Example:
Visiting: (row, column) | g = ... | h = ... | f = ...
After the search, a result summary is displayed.
Example:
============================================================
                         RESULT
============================================================

Status          : SUCCESS
Algorithm       : A*
Start           : (1, 1)
Goal            : (10, 10)
Path length     : ...
Cells explored  : ...
Execution time  : ... sec
Heuristic       : Manhattan
If no valid route is found, the program reports that no path is available.
The exact values depend on the generated maze.

⚙️ Configuration
The main configuration values are defined in:
maze_test.py
Typical configuration includes:
Variable
Default
Description
ROWS
10
Number of maze rows
COLS
10
Number of maze columns
START
(1, 1)
Starting position
GOAL
(10, 10)
Destination position
EXPLORATION_DELAY
180 ms
Exploration animation delay
FINAL_PATH_DELAY
700 ms
Final path animation delay
Changing the Maze Size
For example:
ROWS = 20
COLS = 20
Changing Exploration Speed
EXPLORATION_DELAY = 500
Changing Final Path Speed
FINAL_PATH_DELAY = 1000
🛠️ Technology Stack
Technology
Purpose
Python
Core programming language
A*
Pathfinding/search algorithm
PyMaze
Maze generation and visualization
heapq
Priority queue
Tkinter Event Loop
Progressive visualization
time
Execution-time measurement
📦 Requirements
The project requires:
Python 3.x
PyMaze 1.0.1
The required dependency is specified in:
requirements.txt
💻 Installation
1. Clone the Repository
git clone https://github.com/PavanM2006/Syntecxhub_MazeSolver_using_A-Search.git
2. Enter the Project Directory
cd Syntecxhub_MazeSolver_using_A-Search
3. Install Dependencies
pip install -r requirements.txt
▶️ Run the Project
Run the Python file included in the repository:
python maze_test.py
The program will:
Generate Maze
     │
     ▼
Start A* Search
     │
     ▼
Explore Maze
     │
     ▼
Record Exploration Order
     │
     ▼
Find Goal
     │
     ▼
Reconstruct Path
     │
     ▼
Visualize Exploration
     │
     ▼
Animate Final Path
📁 Project Structure
Syntecxhub_MazeSolver_using_A-Search/
│
├── maze_test.py
│   └── Main Python implementation
│       • Maze generation
│       • A* search
│       • Manhattan heuristic
│       • Path reconstruction
│       • Search visualization
│       • Agent animation
│
├── requirements.txt
│   └── Project dependencies
│
├── README.md
│   └── Project documentation
│
└── .gitignore
    └── Git version-control exclusions
maze_test.py
Contains the main implementation of the maze solver, including maze generation, A* search, heuristic calculation, exploration tracking, path reconstruction, visualization, and agent animation.
requirements.txt
Contains the Python package required to run the project.
README.md
Contains the complete documentation for the project.
.gitignore
Specifies files and directories that should not be tracked by Git.
⏱️ Complexity Analysis
Let:
V = number of maze cells
E = number of valid connections between cells
Time Complexity
With a binary-heap priority queue, the general graph-search formulation has:
O(E log V)
Space Complexity
The algorithm stores the open list, closed set, score mappings, parent relationships, and exploration order.
Therefore:
O(V)
💡 Why A*?
A* is useful because it combines information about the path already travelled with an estimate of the remaining distance.
Actual Cost
     +
Estimated Remaining Cost
     =
Search Priority
In this project:
f(n) = g(n) + h(n)
The Manhattan Distance heuristic helps guide the search toward the goal instead of exploring the maze without direction.
🌍 Real-World Applications
The pathfinding concepts demonstrated by this project can be applied to:
🤖 Robot navigation
🎮 Game AI
🗺️ Route planning
🚗 Navigation systems
📦 Warehouse automation
🚁 Drone pathfinding
🚀 Autonomous systems
🧪 AI simulations
🦾 Robotics
🎯 Project Highlights
This project demonstrates practical implementation of:
Artificial Intelligence
Informed search
Heuristic search
A* pathfinding
State-space exploration
Goal-directed search
Data Structures
Priority Queue
Heap
Set
Dictionary
List
Python Programming
Functions
Tuples
Dictionaries
Sets
Lists
Modules
Performance measurement
Visualization
PyMaze
Tkinter event scheduling
Progressive animation
Agent path tracing
📚 Learning Outcomes
By developing this project, the following concepts can be understood practically:
How A* search works.
How heuristic functions guide AI search.
How priority queues are used in pathfinding.
How g(n), h(n), and f(n) influence search decisions.
How paths can be reconstructed using parent relationships.
How algorithm execution can be visualized.
How search performance can be measured.
How Python data structures can be combined to implement AI algorithms.
🔮 Future Improvements
Possible improvements include:
[ ] Interactive maze generation
[ ] User-defined start and goal positions
[ ] Manual wall placement
[ ] Diagonal movement
[ ] Alternative heuristic functions
[ ] BFS vs DFS vs Dijkstra vs A* comparison
[ ] Real-time open/closed set statistics
[ ] Interactive animation controls
[ ] Command-line configuration
[ ] GIF/MP4 visualization export
[ ] Improved graphical interface
[ ] Multiple maze-size options
