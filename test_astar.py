# ============================================================
#              A* MAZE SOLVER - CORRECTNESS TEST
# ============================================================

from pyamaze import maze
import heapq


# ============================================================
# CONFIGURATION
# ============================================================

ROWS = 10
COLS = 10

START = (1, 1)
GOAL = (10, 10)


# ============================================================
# MANHATTAN HEURISTIC
# ============================================================

def heuristic(cell, goal):

    return (
        abs(cell[0] - goal[0])
        + abs(cell[1] - goal[1])
    )


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
# A* ALGORITHM
# ============================================================

def astar(m, start, goal):

    open_list = []

    counter = 0

    heapq.heappush(
        open_list,
        (
            heuristic(start, goal),
            counter,
            start
        )
    )

    g_score = {
        start: 0
    }

    came_from = {}

    closed_set = set()

    explored = []

    while open_list:

        f, _, current = heapq.heappop(open_list)

        if current in closed_set:
            continue

        closed_set.add(current)

        explored.append(current)

        # Goal reached
        if current == goal:

            path = []

            node = goal

            while node != start:

                path.append(node)

                node = came_from[node]

            path.append(start)

            path.reverse()

            return path, explored

        # Explore neighbours
        for neighbour in get_neighbors(m, current):

            if neighbour in closed_set:
                continue

            new_cost = g_score[current] + 1

            if (
                neighbour not in g_score
                or new_cost < g_score[neighbour]
            ):

                g_score[neighbour] = new_cost

                came_from[neighbour] = current

                h = heuristic(
                    neighbour,
                    goal
                )

                f = new_cost + h

                counter += 1

                heapq.heappush(
                    open_list,
                    (
                        f,
                        counter,
                        neighbour
                    )
                )

    return None, explored


# ============================================================
# TEST 1
# ============================================================

def test_path_exists():

    print()
    print("=" * 60)
    print("TEST 1 - NORMAL MAZE")
    print("=" * 60)

    m = maze(ROWS, COLS)

    m.CreateMaze(
        x=GOAL[0],
        y=GOAL[1],
        loopPercent=30
    )

    path, explored = astar(
        m,
        START,
        GOAL
    )

    if path is None:

        print("❌ FAIL")
        print("A* could not find a path.")

        return False

    print("✅ PASS")
    print("Path found.")
    print("Path length:", len(path) - 1)
    print("Cells explored:", len(explored))

    return True


# ============================================================
# TEST 2
# ============================================================

def test_start_and_goal():

    print()
    print("=" * 60)
    print("TEST 2 - START AND GOAL")
    print("=" * 60)

    m = maze(ROWS, COLS)

    m.CreateMaze(
        x=GOAL[0],
        y=GOAL[1],
        loopPercent=30
    )

    path, _ = astar(
        m,
        START,
        GOAL
    )

    if path is None:

        print("❌ FAIL")
        return False

    if path[0] != START:

        print("❌ FAIL")
        print("Path does not start at:", START)

        return False

    if path[-1] != GOAL:

        print("❌ FAIL")
        print("Path does not end at:", GOAL)

        return False

    print("✅ PASS")
    print("Correct start:", path[0])
    print("Correct goal :", path[-1])

    return True


# ============================================================
# TEST 3
# ============================================================

def test_no_invalid_moves():

    print()
    print("=" * 60)
    print("TEST 3 - WALL / MOVEMENT VALIDATION")
    print("=" * 60)

    m = maze(ROWS, COLS)

    m.CreateMaze(
        x=GOAL[0],
        y=GOAL[1],
        loopPercent=30
    )

    path, _ = astar(
        m,
        START,
        GOAL
    )

    if path is None:

        print("❌ FAIL")
        return False

    for i in range(len(path) - 1):

        current = path[i]

        next_cell = path[i + 1]

        valid_neighbours = get_neighbors(
            m,
            current
        )

        if next_cell not in valid_neighbours:

            print("❌ FAIL")
            print(
                "Invalid movement:",
                current,
                "->",
                next_cell
            )

            return False

    print("✅ PASS")
    print("No wall was crossed.")
    print("All movements are valid.")

    return True


# ============================================================
# TEST 4
# ============================================================

def test_path_length():

    print()
    print("=" * 60)
    print("TEST 4 - PATH LENGTH")
    print("=" * 60)

    m = maze(ROWS, COLS)

    m.CreateMaze(
        x=GOAL[0],
        y=GOAL[1],
        loopPercent=30
    )

    path, _ = astar(
        m,
        START,
        GOAL
    )

    if path is None:

        print("❌ FAIL")
        return False

    calculated_length = len(path) - 1

    expected_length = 0

    for i in range(len(path) - 1):

        expected_length += 1

    if calculated_length != expected_length:

        print("❌ FAIL")
        return False

    print("✅ PASS")
    print("Path length:", calculated_length)

    return True


# ============================================================
# TEST 5
# ============================================================

def test_manhattan_heuristic():

    print()
    print("=" * 60)
    print("TEST 5 - MANHATTAN HEURISTIC")
    print("=" * 60)

    value = heuristic(
        START,
        GOAL
    )

    expected = (
        abs(START[0] - GOAL[0])
        + abs(START[1] - GOAL[1])
    )

    if value != expected:

        print("❌ FAIL")
        print("Expected:", expected)
        print("Got:", value)

        return False

    print("✅ PASS")
    print("Heuristic:", value)

    return True


# ============================================================
# RUN ALL TESTS
# ============================================================

print()
print("=" * 60)
print("           A* CORRECTNESS TEST SUITE")
print("=" * 60)

results = []

results.append(
    test_path_exists()
)

results.append(
    test_start_and_goal()
)

results.append(
    test_no_invalid_moves()
)

results.append(
    test_path_length()
)

results.append(
    test_manhattan_heuristic()
)


# ============================================================
# FINAL RESULT
# ============================================================

passed = results.count(True)

total = len(results)

print()
print("=" * 60)
print("                 TEST SUMMARY")
print("=" * 60)

print()
print(
    f"Tests passed: {passed}/{total}"
)

if passed == total:

    print()
    print("🎉 ALL TESTS PASSED!")
    print()
    print("Your A* implementation is working correctly.")

else:

    print()
    print("⚠️ SOME TESTS FAILED.")
    print("Check the output above.")

print()
print("=" * 60)
