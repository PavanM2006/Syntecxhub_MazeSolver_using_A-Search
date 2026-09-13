# A* Maze Solver — Progressive Exploration Visualizer

A Python project that solves a randomly generated maze using the **A\* search algorithm** and visually animates the entire process — first showing every cell the algorithm explores, step by step, then tracing the final optimal path from start to goal.

Built with [`pyamaze`](https://pypi.org/project/pyamaze/) for maze generation and rendering.

---

## Features

- **A\* pathfinding** using a Manhattan-distance heuristic
- **Priority-queue search** implemented with Python's `heapq`
- **Progressive exploration animation** — cells light up in the exact order A* visits them
- **Animated final path trace** once the goal is reached
- **Detailed console logging** of every visited cell (`g`, `h`, `f` scores) and a final results summary
- **Fully configurable** maze size, start/goal positions, and animation speed
- Handles the **no-path-found** case gracefully

---

## Visualization Legend

| Marker | Meaning |
|---|---|
| 🔴 Red square | Start cell |
| 🟢 Green square | Goal cell |
| 🔵 Blue arrow | A* agent |
| 🔵 Blue-marked cells | Cells explored during the search |
| ⚪ White footprints | Agent's movement trail along the final path |

---

## Requirements

- Python 3.x
- [`pyamaze`](https://pypi.org/project/pyamaze/)

## Installation

```bash
pip install pyamaze
```

## Usage

```bash
python astar_maze_solver.py
```

Running the script will:
1. Generate a random maze with loops
2. Run A* search from `START` to `GOAL`, printing each visited cell to the console
3. Print a summary (status, path length, cells explored, execution time)
4. Open a graphical window and animate the exploration, followed by the agent tracing the final path

---

## How It Works

### 1. Maze Generation
A `ROWS x COLS` maze is created with `pyamaze.maze()`, using `loopPercent=30` to introduce loops (multiple possible paths) rather than a single perfect-maze solution.

### 2. A* Search (`astar`)
- **Heuristic:** Manhattan distance — `|x1 - x2| + |y1 - y2|` — admissible for grid movement with no diagonals.
- **Open list:** a min-heap keyed on `(f_score, insertion_counter, cell)`. The counter breaks ties deterministically and avoids comparing cell tuples directly.
- **Closed set:** tracks fully-expanded cells to avoid reprocessing.
- **g_score / came_from:** standard A* bookkeeping for path cost and path reconstruction.
- **exploration_order:** every cell is appended here the moment it's popped off the open list — this list drives the visualization later.
- When the goal is popped, the path is reconstructed by walking `came_from` backward from goal to start, then reversed.

### 3. Neighbor Lookup (`get_neighbors`)
Reads the `E`/`W`/`N`/`S` wall flags from `pyamaze`'s `maze_map` for a given cell and returns only the directions that are open (no wall).

### 4. Visualization Pipeline
Since `pyamaze` doesn't support step-by-step exploration animation natively, this project builds it manually on top of the Tkinter event loop:

- `show_exploration(index)` recursively schedules itself via `m._win.after(EXPLORATION_DELAY, ...)`, revealing one more explored cell each call by updating `m.markCells`.
- Once every explored cell has been shown, `start_agent_animation()` is scheduled, which calls `m.tracePath()` to animate the agent walking the final path with footprints (`showMarked=True` keeps the exploration markings visible underneath).

This avoids manual `canvas.move()`/`coords()` calls entirely, relying on `pyamaze`'s built-in `tracePath()` for the final movement.

---

## Configuration

All key parameters are defined at the top of the script:

| Variable | Default | Description |
|---|---|---|
| `ROWS` | `10` | Number of maze rows |
| `COLS` | `10` | Number of maze columns |
| `START` | `(1, 1)` | Starting cell |
| `GOAL` | `(10, 10)` | Goal cell |
| `EXPLORATION_DELAY` | `180` ms | Delay between revealing each explored cell |
| `FINAL_PATH_DELAY` | `700` ms | Delay between agent steps along the final path |

Increase the delays to slow the animation down for presentations, or decrease them for a faster demo.

---

## Sample Console Output

```
============================================================
                  A* SEARCH
============================================================
Visiting: (1, 1) | g = 0 | h = 18 | f = 18
Visiting: (1, 2) | g = 1 | h = 17 | f = 18
...
Goal reached!

============================================================
                     RESULT
============================================================
Status         : SUCCESS
Algorithm      : A*
Start          : (1, 1)
Goal           : (10, 10)
Path length    : 18
Cells explored : 42
Execution time : 0.001532 sec
Heuristic      : Manhattan

Final A* Path
----------------------------------------
00 -> (1, 1)
01 -> (1, 2)
...
```

---

## Project Structure

```
.
└── astar_maze_solver.py   # Single-file implementation: maze setup, A* search, and visualization
```

## Time & Space Complexity

- **Time:** `O(E log V)` in the worst case, where `V` is the number of cells and `E` the number of open passages, due to heap push/pop operations.
- **Space:** `O(V)` for the open list, closed set, and score dictionaries.

## Possible Improvements

- Support diagonal movement (8-directional)
- Swap in alternative heuristics (Euclidean, Chebyshev) for comparison
- Add a live open-list/closed-list counter overlay in the GUI
- Export the animation as a GIF/MP4
- Parameterize maze size and delays via command-line arguments

## License

This project is open for personal and academic use.
