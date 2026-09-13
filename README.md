# 🧠 A* Maze Solver with AI Search Visualization

A Python-based Artificial Intelligence project that demonstrates the **A\* (A-Star) search algorithm** by solving a dynamically generated maze and visually showing how the algorithm explores the maze before following the final path to the goal.

The project is designed as an educational and portfolio project to demonstrate fundamental **AI search, pathfinding, heuristics, graph traversal, and algorithm visualization** concepts.

---

## 🚀 Project Overview

The program generates a maze using the `pyamaze` library and uses the **A\* search algorithm** to find a path from a starting cell to a goal cell.

Instead of displaying only the final solution, the project visualizes the A\* search process:

1. The maze is generated dynamically.
2. A\* starts from the starting cell.
3. The algorithm evaluates available neighbouring cells.
4. Explored/search cells are displayed.
5. A\* uses the Manhattan distance heuristic to make decisions.
6. The optimal path is reconstructed after reaching the goal.
7. The blue A\* agent follows the final path using `pyamaze`'s built-in movement system.
8. White footprints show the agent's movement.

This makes the project useful for understanding **how A\* actually searches for a solution**.

---

## 🎯 Objectives

The main objectives of this project are:

- Implement the A\* search algorithm from scratch.
- Understand heuristic-based search.
- Use Manhattan distance as an admissible heuristic for 4-directional movement.
- Generate and solve dynamic mazes.
- Visualize A\* exploration.
- Visualize the final path.
- Demonstrate `g(n)`, `h(n)` and `f(n)` values.
- Measure algorithm execution time.
- Demonstrate AI pathfinding in a visual and understandable way.

---

## 🧩 Technologies Used

- **Python 3**
- **A\* Search Algorithm**
- **Manhattan Distance Heuristic**
- **pyamaze**
- **Tkinter**
- **heapq**
- **time**
- **Termux + Termux:X11** for Android-based development/testing

---

## 🧠 How A* Works

A\* evaluates each candidate cell using:

```text
f(n) = g(n) + h(n)
