# 🧠 A* Maze Solver with AI Search Visualization

A Python-based Artificial Intelligence project that demonstrates the
A* (A-Star) search algorithm by solving a dynamically generated maze.

The project visualizes the A* search process, showing the cells explored
by the algorithm before displaying and animating the final path from the
start position to the goal.

---

## 🚀 Project Overview

The A* algorithm is a popular pathfinding and graph-search algorithm
used in Artificial Intelligence, robotics, games, navigation systems,
and autonomous systems.

This project demonstrates how A* can:

1. Generate a maze environment
2. Start searching from the start cell
3. Explore possible routes
4. Calculate the cost of each cell
5. Use a heuristic to guide the search
6. Reach the goal
7. Reconstruct the optimal path
8. Visually animate the agent following that path

---

## ✨ Features

- A* search algorithm
- Manhattan distance heuristic
- Dynamically generated maze
- Configurable maze size
- Maze walls generated using `pyamaze`
- Visual exploration of A* search
- Final path reconstruction
- Animated A* agent
- Agent footprints
- Start marker
- Goal marker
- Explored-cell visualization
- Path-length calculation
- Number of explored cells
- Execution-time measurement
- Terminal search information
- Graphical visualization
- No manual Canvas movement
- Uses pyamaze's built-in agent movement

---

## 🎨 Visualization

The visualization uses `pyamaze` agents and maze rendering.

### Markers

- 🔴 **Red** = Start
- 🔵 **Blue** = A* Agent
- 🟢 **Green** = Goal
- 🔵 **Marked cells** = A* explored/search area
- ⚪ **Footprints** = Agent movement history

> The final path is displayed using `pyamaze`'s built-in
> `tracePath()` functionality. The project does not manually assign
> a yellow/orange color to the final path.

---

## 🧠 A* Search Algorithm

A* evaluates each cell using:

    f(n) = g(n) + h(n)

Where:

- `g(n)` = actual cost from the start to the current cell
- `h(n)` = estimated cost from the current cell to the goal
- `f(n)` = estimated total cost of the route

The cell with the lowest estimated total cost is selected for further
exploration.

---

## 📐 Manhattan Heuristic

This project uses the Manhattan distance heuristic:

    h(n) = |x1 - x2| + |y1 - y2|

The heuristic is suitable for this project because the agent moves
through the maze in four directions:

- North
- South
- East
- West

Diagonal movement is not used.

---

## 🔍 A* Exploration Visualization

Unlike a basic pathfinding program that only displays the final route,
this project visualizes the search process.

The terminal displays information such as:

    Visiting: (4, 3) | g = 5 | h = 13 | f = 18

Where:

    g = distance travelled
    h = estimated distance to goal
    f = total estimated cost

The graphical interface also displays the explored cells.

This makes it possible to observe how A* searches through the maze
before reaching the final solution.

---

## 🗺️ Maze Generation

The maze is generated using the `pyamaze` library.

The current configuration uses:

    ROWS = 10
    COLS = 10

The maze is created with:

    loopPercent = 30

This allows alternative routes in the maze and provides a more
interesting environment for demonstrating A* search.

---

## 🤖 Agent Movement

The project uses the built-in `pyamaze.agent` class.

The agent is not moved using manual Canvas coordinate calculations.

The final route is passed to:

    m.tracePath()

This allows `pyamaze` to control the agent's movement through the
maze.

The animation speed is controlled using:

    FINAL_PATH_DELAY = 700

A higher value produces slower movement.

---

## 📊 Program Output

The program reports information such as:

    Algorithm      : A*
    Start          : (1, 1)
    Goal           : (10, 10)
    Path length    : XX
    Cells explored : XX
    Execution time : X.XXXXXX sec
    Heuristic      : Manhattan

The exact path length and number of explored cells may change because
the maze is dynamically generated.

---

## 🧪 Correctness Testing

A separate testing program is included:

    test_astar.py

Run it using:

    python test_astar.py

The test suite verifies:

- Path existence
- Correct start position
- Correct goal position
- Valid movement between cells
- No wall crossing
- Correct path length calculation
- Manhattan heuristic calculation

---

## 🛠️ Technologies Used

- Python
- A* Search
- Priority Queue
- `heapq`
- Manhattan Heuristic
- pyamaze
- Tkinter
- Termux
- Termux:X11

---

## 📂 Project Structure

    Project1_AStar/
    │
    ├── maze_test.py
    ├── test_astar.py
    ├── requirements.txt
    ├── README.md
    │
    └── screenshots/

---

## ▶️ Installation

Install the required Python package:

    pip install -r requirements.txt

The project currently requires:

    pyamaze==1.0.1

---

## ▶️ Running the Project

### Step 1 — Open the project directory

    cd ~/AI_Projects/Project1_AStar

### Step 2 — Set the display

For Termux:X11:

    export DISPLAY=:1

### Step 3 — Run the A* solver

    python maze_test.py

---

## 🧪 Running the Tests

To run the correctness tests:

    python test_astar.py

---

## 💡 Why This Is an AI Project

The project demonstrates a fundamental Artificial Intelligence
technique: intelligent search.

Instead of blindly moving through the maze, A* evaluates possible
states using both:

    Actual cost + Estimated future cost

This allows the algorithm to efficiently search for an optimal path.

The project therefore demonstrates concepts including:

- State-space search
- Heuristics
- Cost functions
- Priority queues
- Path optimization
- Search-space exploration
- Goal-directed decision making

---

## 🎯 Learning Objectives

This project was developed to understand:

1. How A* search works
2. How heuristic functions guide AI search
3. How priority queues are used in A*
4. How paths can be reconstructed
5. How search algorithms explore a state space
6. How AI algorithms can be visualized
7. How Python libraries can be integrated into an AI project

---

## 🔮 Future Improvements

Possible future improvements include:

- Interactive maze generation
- Adjustable maze size
- Adjustable animation speed
- User-selected start and goal
- Different obstacle types
- Weighted maze cells
- Performance analysis
- Web-based visualization
- Interactive graphical controls

---

## 📌 Project Status

**Status: Completed Core A* Visualization Project**

The current version successfully:

- Generates a maze
- Runs A* search
- Uses Manhattan heuristic
- Visualizes explored cells
- Reconstructs the final path
- Animates the agent
- Displays search statistics

