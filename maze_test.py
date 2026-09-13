# ============================================================
#                 A* MAZE SOLVER - STEP 7
#          PROGRESSIVE A* EXPLORATION VISUALIZATION
# ============================================================

from pyamaze import maze, agent, COLOR
import heapq
import time


# ============================================================
# CONFIGURATION
# ============================================================

ROWS = 10
COLS = 10

START = (1, 1)
GOAL = (10, 10)

# Slow exploration
EXPLORATION_DELAY = 180

# Slow final agent movement
FINAL_PATH_DELAY = 700


# ============================================================
# A* HEURISTIC
# ============================================================

def heuristic(cell, goal):
    return abs(cell[0] - goal[0]) + abs(cell[1] - goal[1])


# ============================================================
# GET VALID NEIGHBOURS
# ============================================================

def get_neighbors(m, cell):

    neighbours = []

    r, c = cell

    if m.maze_map[cell]['E'] == 1:
        neighbours.append((r, c + 1))

    if m.maze_map[cell]['W'] == 1:
        neighbours.append((r, c - 1))

    if m.maze_map[cell]['N'] == 1:
        neighbours.append((r - 1, c))

    if m.maze_map[cell]['S'] == 1:
        neighbours.append((r + 1, c))

    return neighbours


# ============================================================
# A* SEARCH
# ============================================================

def astar(m, start, goal):

    print()
    print("=" * 60)
    print("                  A* SEARCH")
    print("=" * 60)

    start_time = time.perf_counter()

    open_list = []

    counter = 0

    h_start = heuristic(start, goal)

    heapq.heappush(
        open_list,
        (h_start, counter, start)
    )

    g_score = {
        start: 0
    }

    came_from = {}

    closed_set = set()

    # IMPORTANT:
    # This stores the exact order in which A*
    # visits cells.
    exploration_order = []

    while open_list:

        f_current, _, current = heapq.heappop(open_list)

        if current in closed_set:
            continue

        closed_set.add(current)

        exploration_order.append(current)

        g_current = g_score[current]

        h_current = heuristic(current, goal)

        print(
            f"Visiting: {current} | "
            f"g = {g_current} | "
            f"h = {h_current} | "
            f"f = {f_current}"
        )

        # ----------------------------------------------------
        # GOAL
        # ----------------------------------------------------

        if current == goal:

            execution_time = (
                time.perf_counter() - start_time
            )

            path = []

            node = goal

            while node != start:

                path.append(node)

                node = came_from[node]

            path.append(start)

            path.reverse()

            print()
            print("Goal reached!")

            return (
                path,
                exploration_order,
                execution_time
            )

        # ----------------------------------------------------
        # NEIGHBOURS
        # ----------------------------------------------------

        for neighbour in get_neighbors(m, current):

            if neighbour in closed_set:
                continue

            tentative_g = g_current + 1

            if (
                neighbour not in g_score
                or tentative_g < g_score[neighbour]
            ):

                came_from[neighbour] = current

                g_score[neighbour] = tentative_g

                h = heuristic(neighbour, goal)

                f = tentative_g + h

                counter += 1

                heapq.heappush(
                    open_list,
                    (f, counter, neighbour)
                )

    execution_time = (
        time.perf_counter() - start_time
    )

    return (
        None,
        exploration_order,
        execution_time
    )


# ============================================================
# CREATE MAZE
# ============================================================

print()
print("=" * 60)
print("                 A* MAZE SOLVER")
print("=" * 60)

print()
print("Creating maze...")

m = maze(ROWS, COLS)

m.CreateMaze(
    x=GOAL[0],
    y=GOAL[1],
    loopPercent=30
)

print("Maze created.")


# ============================================================
# RUN A*
# ============================================================

path, explored, execution_time = astar(
    m,
    START,
    GOAL
)


# ============================================================
# RESULT
# ============================================================

print()
print("=" * 60)
print("                     RESULT")
print("=" * 60)

if path is None:

    print()
    print("Status         : NO PATH")
    print("Algorithm      : A*")
    print("Start          :", START)
    print("Goal           :", GOAL)
    print("Cells explored :", len(explored))
    print(
        "Execution time : "
        f"{execution_time:.6f} sec"
    )
    print("Heuristic      : Manhattan")

else:

    path_length = len(path) - 1

    print()
    print("Status         : SUCCESS")
    print("Algorithm      : A*")
    print("Start          :", START)
    print("Goal           :", GOAL)
    print("Path length    :", path_length)
    print("Cells explored :", len(explored))
    print(
        "Execution time : "
        f"{execution_time:.6f} sec"
    )
    print("Heuristic      : Manhattan")

    print()
    print("Final A* Path")
    print("-" * 40)

    for i, cell in enumerate(path):

        print(
            f"{i:02d} -> {cell}"
        )


# ============================================================
# CREATE START MARKER
# ============================================================

start_agent = agent(
    m,
    x=START[0],
    y=START[1],
    color=COLOR.red,
    filled=True,
    shape='square'
)


# ============================================================
# CREATE GOAL MARKER
# ============================================================

goal_agent = agent(
    m,
    x=GOAL[0],
    y=GOAL[1],
    color=COLOR.green,
    filled=True,
    shape='square'
)


# ============================================================
# CREATE A* AGENT
# ============================================================

a = agent(
    m,
    x=START[0],
    y=START[1],
    color=COLOR.blue,
    filled=True,
    shape='arrow',
    footprints=True
)


# ============================================================
# VISUALIZATION
# ============================================================

if path is None:

    print()
    print("=" * 60)
    print("                 VISUALIZATION")
    print("=" * 60)

    print()
    print("No path exists.")
    print("Displaying maze...")

    m.run()

else:

    print()
    print("=" * 60)
    print("             A* EXPLORATION")
    print("=" * 60)

    print()
    print("RED    = Start")
    print("BLUE   = A* Agent")
    print("GREEN  = Goal")
    print("BLUE MARKS = Explored cells")
    print("YELLOW = Final optimal path")
    print("WHITE FOOTPRINTS = Agent movement")

    print()
    print("Starting graphical visualization...")


    # ========================================================
    # PROGRESSIVE EXPLORATION
    # ========================================================
    #
    # We use pyamaze's markCells system.
    #
    # The maze is first shown.
    # Then explored cells are added progressively.
    #
    # No Canvas movement is used.
    #

    def show_exploration(index=0):

        if index >= len(explored):

            print()
            print("A* exploration complete.")

            # ------------------------------------------------
            # FINAL PATH
            # ------------------------------------------------

            print("Displaying final optimal path...")

            # Mark final path
            m.markCells = path

            # Small delay before agent starts
            m._win.after(
                1000,
                start_agent_animation
            )

            return


        current_cell = explored[index]

        # Don't overwrite start/goal markers
        if (
            current_cell != START
            and current_cell != GOAL
        ):

            # Add the current explored cell
            m.markCells = explored[:index + 1]

        print(
            f"Exploring "
            f"{index + 1}/{len(explored)} : "
            f"{current_cell}"
        )

        # Schedule next exploration step
        m._win.after(
            EXPLORATION_DELAY,
            lambda: show_exploration(index + 1)
        )


    # ========================================================
    # FINAL AGENT MOVEMENT
    # ========================================================

    def start_agent_animation():

        print()
        print("=" * 60)
        print("              FINAL A* PATH")
        print("=" * 60)

        print()
        print(
            "Agent is now following "
            "the optimal A* path..."
        )

        #
        # IMPORTANT:
        #
        # pyamaze tracePath() performs the movement.
        #
        # We do NOT use:
        #
        # canvas.move()
        # canvas.coords()
        # moveRight()
        # moveLeft()
        # moveUp()
        # moveDown()
        #
        # This prevents the previous movement problems.
        #

        m.tracePath(
            {a: path},
            delay=FINAL_PATH_DELAY,
            showMarked=True,
            kill=False
        )


    # ========================================================
    # START GUI
    # ========================================================

    print()
    print("Opening maze window...")

    #
    # Run the Tkinter event loop.
    #
    # The exploration animation starts after the window
    # has been created.
    #

    m._win.after(
        1000,
        lambda: show_exploration(0)
    )

    m.run()
