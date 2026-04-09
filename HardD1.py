"""
MaRS Recruitment - Hard Dose Q1
Rover Brick Arena Navigation

Tasks:
  1. Read obstacle positions from a .txt file
  2. Build an n x n arena map (0=obstacle, 1=safe)
  3. Print the arena matrix
  4. BONUS: Find shortest path from [0,0] to [10,10] using BFS

File Format (each row = one obstacle):
  col1=North distance, col2=East distance,
  col3=South distance, col4=West distance
  from the initial position (0,0).
"""

from collections import deque

ARENA_SIZE = 11  # 11x11 to include indices 0..10


def load_obstacles(filepath: str) -> list:
    """Parse obstacle file. Returns list of (row, col) obstacle positions."""
    obstacles = []
    start_r, start_c = 0, 0

    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = list(map(int, line.split()))
            if len(parts) < 4:
                continue
            north, east, south, west = parts

            # Convert directional distances to grid coordinates
            positions = [
                (start_r - north, start_c),  # North
                (start_r, start_c + east),   # East
                (start_r + south, start_c),  # South
                (start_r, start_c - west),   # West
            ]
            for r, c in positions:
                if 0 <= r < ARENA_SIZE and 0 <= c < ARENA_SIZE:
                    obstacles.append((r, c))

    return list(set(obstacles))  # Remove duplicates


def build_arena(obstacles: list, size: int) -> list:
    """Create size x size grid. 1 = safe, 0 = obstacle."""
    arena = [[1] * size for _ in range(size)]
    for r, c in obstacles:
        if 0 <= r < size and 0 <= c < size:
            arena[r][c] = 0
    return arena


def print_arena(arena: list, path: list = None):
    """
    Print a clean visual map.
    Obstacles: , Safe: ··, Path: ●● (or S / D for start/dest)
    """
    path_set = set(path) if path else set()
    size = len(arena)

    # Top border
    print("   +" + "---" * size + "+")
    # Column numbers
    print("    ", end="")
    for c in range(size):
        print(f"{c:^3}", end="")
    print("\n   +" + "---" * size + "+")

    for r in range(size):
        print(f"{r:2d} |", end="")
        for c in range(size):
            if (r, c) == (0, 0):
                cell = " S "
            elif (r, c) == (10, 10):
                cell = " D "
            elif (r, c) in path_set:
                cell = " ● "
            elif arena[r][c] == 0:
                cell = ""
            else:
                cell = " · "
            print(cell, end="")
        print("|")
    print("   +" + "---" * size + "+")


def bfs_shortest_path(arena: list, start: tuple, goal: tuple):
    """
    BFS for shortest path (up, down, left, right only).
    Returns list of (row, col) or None if unreachable.
    """
    size = len(arena)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    queue = deque()
    queue.append((start, [start]))
    visited = {start}

    while queue:
        (r, c), path = queue.popleft()
        if (r, c) == goal:
            return path

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (0 <= nr < size and 0 <= nc < size and
                    arena[nr][nc] == 1 and (nr, nc) not in visited):
                visited.add((nr, nc))
                queue.append(((nr, nc), path + [(nr, nc)]))

    return None


# ------------------------------------------------------------
# MAIN
# ------------------------------------------------------------
if __name__ == "__main__":
    import os

    sample_file = "sample.txt"

    if os.path.exists(sample_file):
        obstacles = load_obstacles(sample_file)
        print(f" Loaded obstacles from {sample_file}: {obstacles}")
    else:
        # Built-in sample from the task description
        sample_data = "2 3 0 3\n5 1 0 2\n3 0 4 4\n3 4 0 2\n"
        with open("sample.txt", "w") as f:
            f.write(sample_data)
        obstacles = load_obstacles("sample.txt")
        print(" Using built-in sample.txt obstacles:", obstacles)

    arena = build_arena(obstacles, ARENA_SIZE)

    print("\n" + "=" * 40)
    print("        ARENA MAP (obstacles = )")
    print("=" * 40)
    print_arena(arena)

    # BONUS: Shortest path
    start = (0, 0)
    goal  = (10, 10)

    print(f"\n{'='*40}")
    print(f"        SHORTEST PATH {start} → {goal}")
    print(f"{'='*40}")

    path = bfs_shortest_path(arena, start, goal)

    if path:
        print(f" Path found! Distance: {len(path) - 1} moves")
        print(f"   Coordinates: {path}")
        print("\n     Arena with path (S=Start, D=Dest, ●=Path):")
        print_arena(arena, path)
    else:
        print(" No path found! Destination is blocked.")