A* Maze Solver — AI Search Visualization

A Python-based Artificial Intelligence project that demonstrates the A (A-Star) Search Algorithm* by solving a dynamically generated maze and progressively visualizing the cells explored by the algorithm before displaying the final path from the starting point to the goal.

The project is designed to provide a practical and visual understanding of informed search, heuristic-based pathfinding, priority queues, and path reconstruction.

---

Project Overview

This repository contains an implementation of the A Search Algorithm* for maze pathfinding.

Instead of displaying only the final solution, the project visualizes the algorithm's search process, allowing users to observe how A* explores the maze and determines the most promising route toward the destination.

The solver uses:

- A Search Algorithm* for pathfinding
- Manhattan Distance as the heuristic
- Python's "heapq" module for priority queue management
- PyMaze for maze generation and visualization
- Progressive visualization of explored cells
- Final path animation after the goal is reached

---

Project Architecture

This repository is structured as a Python-based AI pathfinding project:

Syntecxhub_MazeSolver_using_A-Search/
│
├── maze_test.py              # Maze / A* implementation
├── requirements.txt          # Required Python dependencies
├── README.md                 # Project documentation
└── .gitignore                # Git ignored files

«The repository intentionally does not reference a separate "astar_maze_solver.py" file. The implementation is contained in the Python source file present in the repository.»

---

Interactive Maze Visualization

When the project is executed, it generates a maze and visually demonstrates the A* search process.

The visualization consists of two major stages:

1. Search Exploration

The algorithm progressively displays the cells explored by A*.

This allows the user to observe:

- Which cells are visited
- The order of exploration
- How the heuristic guides the search
- How A* moves toward the goal

2. Final Path

After the goal is reached, the algorithm reconstructs the path using the stored parent relationships and displays the final route from the starting position to the destination.

START
  │
  ▼
Generate Maze
  │
  ▼
Initialize A*
  │
  ▼
Select Lowest f(n)
  │
  ▼
Explore Neighbours
  │
  ▼
Calculate g(n), h(n), f(n)
  │
  ├───────────────┐
  │               │
  ▼               ▼
Goal reached?    No
  │               │
 Yes              └──────► Continue Search
  │
  ▼
Reconstruct Path
  │
  ▼
Display Final Path

---

Detailed Features

🤖 A* Search Algorithm

The project implements the A informed search algorithm* to find an efficient path between the starting point and the destination.

A* evaluates each cell using:

f(n) = g(n) + h(n)

Where:

- "g(n)" = Cost from the starting cell to the current cell
- "h(n)" = Estimated cost from the current cell to the goal
- "f(n)" = Estimated total cost

The cell with the lowest "f(n)" value is prioritized for exploration.

---

🧮 Manhattan Distance Heuristic

The project uses Manhattan Distance as the heuristic function.

h(n) = |x1 - x2| + |y1 - y2|

This heuristic is suitable for the grid-based maze because movement is performed in four directions.

        ↑
        │
←───────┼───────→
        │
        ↓

Diagonal movement is not considered.

---

🔍 Progressive Search Visualization

The project records the order in which cells are explored.

Instead of immediately showing the final result, the exploration process is displayed progressively.

Conceptually:

Cell 1
   ↓
Cell 2
   ↓
Cell 3
   ↓
Cell 4
   ↓
   .
   .
   .
   ↓
Goal

This makes the project particularly useful for understanding the internal behavior of A*.

---

🎯 Final Path Reconstruction

Once the goal is reached, the algorithm reconstructs the path using the stored parent relationships.

The path is initially reconstructed from:

GOAL → Parent → Parent → ... → START

and then reversed into:

START → ... → GOAL

The final route is then visually displayed.

---

🎲 Dynamic Maze Generation

The project generates a maze dynamically rather than relying on a fixed hard-coded maze.

This allows the A* algorithm to operate on different maze configurations and search through different possible routes.

---

⛏️ Priority Queue

Python's built-in "heapq" module is used to implement the priority queue required by A*.

The priority is based on the calculated "f(n)" value.

This allows the algorithm to efficiently select the most promising cell for the next exploration step.

---

📊 Search Statistics

The program provides search-related information through the console, including details such as:

- Algorithm used
- Start position
- Goal position
- Path information
- Number of explored cells
- Execution time
- Heuristic used

The exact values depend on the dynamically generated maze.

---

🚫 No-Path Handling

The implementation also handles cases where the goal cannot be reached.

If no valid route exists, the solver reports that a path could not be found instead of attempting to reconstruct an invalid route.

---

Technology Stack

Technology| Purpose
Python| Core programming language
A*| AI search and pathfinding
PyMaze| Maze generation and visualization
heapq| Priority queue
Manhattan Distance| Heuristic function

---

How A* Works in This Project

The search process follows the following approach:

Step 1 — Initialize Search

The starting cell is inserted into the priority queue.

The initial cost is:

g(start) = 0

The heuristic is calculated using the Manhattan distance to the goal.

---

Step 2 — Select Best Candidate

The algorithm removes the cell with the lowest:

f(n) = g(n) + h(n)

from the priority queue.

---

Step 3 — Explore Neighbours

The algorithm checks the available neighbouring cells.

For the four-directional grid:

        North
          ↑
          │
West ← Current → East
          │
          ↓
        South

Blocked or inaccessible cells are ignored.

---

Step 4 — Calculate New Cost

For each valid neighbour, the algorithm calculates the tentative path cost.

If the newly discovered route is better than the previously recorded route, the corresponding score and parent information are updated.

---

Step 5 — Continue Until Goal

The process continues until:

Current Cell == Goal

or until there are no remaining nodes to explore.

---

Step 6 — Reconstruct Solution

After reaching the goal, the stored parent relationships are used to reconstruct the final path.

---

Data Structures Used

The implementation uses several important data structures.

Priority Queue
Used to select the next cell with the lowest estimated total cost.

heapq

Closed Set
Tracks cells that have already been explored.

"g_score"
Stores the currently known cost from the starting point to each cell.

"came_from"
Stores the parent relationship used for final path reconstruction.

Exploration Order
Stores the sequence of explored cells so that the search can be visualized progressively.

---
 Visualization Flow

```text
┌─────────────────────────────┐
│       Generate Maze         │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│       Start A* Search       │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│    Calculate f(n) = g + h   │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│     Select Best Candidate   │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│    Explore Neighbour Cells  │
└──────────────┬──────────────┘
               │
               ▼
        ┌───────────────┐
        │  Goal Found?  │
        └───────┬───────┘
                │
          ┌─────┴─────┐
          │           │
         No          Yes
          │           │
          │           ▼
          │    ┌───────────────┐
          │    │ Reconstruct   │
          │    │     Path      │
          │    └───────┬───────┘
          │            │
          └────────────┤
                       ▼
              ┌──────────────────┐
              │ Display Solution │
              └──────────────────┘

---

Project Structure

Syntecxhub_MazeSolver_using_A-Search/
│
├── maze_test.py
├── requirements.txt
├── README.md
└── .gitignore

"maze_test.py"

Contains the Python implementation of the maze-solving system, including the A search logic and maze visualization*.

"requirements.txt"

Contains the Python packages required to install and run the project.

"README.md"

Provides complete project documentation, including the project overview, features, algorithm explanation, installation instructions, usage, and implementation details.

".gitignore"

Specifies files and directories that should be excluded from Git version control.

---

Local Installation

1. Clone the Repository

git clone https://github.com/PavanM2006/Syntecxhub_MazeSolver_using_A-Search.git

2. Navigate to the Project

cd Syntecxhub_MazeSolver_using_A-Search

3. Install Dependencies

pip install -r requirements.txt

If required, the PyMaze dependency can also be installed directly:

pip install pyamaze

---

Running the Project

Run the Python source file included in the repository:

python maze_test.py

«If your local repository uses a different Python source filename, run that file instead.»

The application should open the maze visualization and begin the A* search process.

---

Example Search Process

A typical execution follows this sequence:

============================================================
                       A* SEARCH
============================================================

Starting Search...

Exploring cells...
Exploring cells...
Exploring cells...
        .
        .
        .

Goal reached!

------------------------------------------------------------
                    SEARCH COMPLETE
------------------------------------------------------------

Path reconstructed successfully.
Final path displayed.

The exact output and path depend on the generated maze.

Complexity Analysis
Let:

- "V" = Number of cells/nodes
- "E" = Number of valid connections between cells

Time Complexity
With a binary-heap priority queue:
O(E log V)

Space Complexity
O(V)

The algorithm maintains information for explored nodes, scores, parent relationships, and the priority queue.

Why A*?
A* provides a balance between:

- Dijkstra's Algorithm, which considers path cost without a heuristic
- Greedy Best-First Search, which relies primarily on the heuristic

A* combines both:

Actual Cost+ Estimated Cost= Total Estimated Cost

This allows it to intelligently prioritize promising paths while still considering the cost already travelled.

Learning Outcomes
This project provides practical experience with:

- Artificial Intelligence search algorithms
- A* pathfinding
- Heuristic functions
- Manhattan distance
- Priority queues
- Python "heapq"
- Graph/state-space search
- Path reconstruction
- Algorithm visualization
- GUI-based animation
- Time and space complexity analysis

Real-World Applications
The concepts demonstrated in this project can be applied to:

- 🤖 Robot navigation
- 🎮 Game AI
- 🗺️ Route planning
- 🚗 Autonomous navigation
- 🏭 Warehouse automation
- 🚁 Drone pathfinding
- 🧭 Navigation systems
- Simulation and robotic

Future Improvements

Possible future enhancements include:

- [ ] Interactive maze generation
- [ ] Manual wall placement
- [ ] User-selectable start and goal positions
- [ ] Diagonal movement support
- [ ] BFS vs DFS vs Dijkstra vs A* comparison
- [ ] Multiple heuristic options
- [ ] Real-time search statistics
- [ ] Improved visualization controls
- [ ] Adjustable animation speed
- [ ] Search performance comparison
- [ ] GIF/video export of the search process
