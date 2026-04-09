from collections import deque
import os

ARENA_SIZE = 11 

def get_arena(filepath):
    # Ensure sample data exists
    if not os.path.exists(filepath):
        with open(filepath, 'w') as f:
            f.write("2 3 0 3\n5 1 0 2\n3 0 4 4\n3 4 0 2\n")
    
    # 1 = Safe position
    arena = [[1] * ARENA_SIZE for _ in range(ARENA_SIZE)]
    with open(filepath, 'r') as f:
        for line in f:
            parts = list(map(int, line.split()))
            if len(parts) == 4:
                n, e, s, w = parts
                # Calculate relative coordinates from (0,0)
                pos = [(0-n, 0), (0, 0+e), (0+s, 0), (0, 0-w)]
                for r, c in pos:
                    if 0 <= r < ARENA_SIZE and 0 <= c < ARENA_SIZE:
                        arena[r][c] = 0 # 0 = Obstacle
    return arena

def get_route(arena, start, goal):
    queue = deque([(start, [start])])
    visited = {start}
    while queue:
        (r, c), path = queue.popleft()
        if (r, c) == goal: return path
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < ARENA_SIZE and 0 <= nc < ARENA_SIZE and \
               arena[nr][nc] == 1 and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append(((nr, nc), path + [(nr, nc)]))
    return None

# --- Main Execution ---
arena = get_arena("sample.txt")
route = get_route(arena, (0, 0), (10, 10))

# OUTPUT 1: The Arena Map
print("OUTPUT 1: Arena Map (0=Obstacle, 1=Safe)")
for row in arena:
    print(" ".join(map(str, row)))

print("\n" + "="*25 + "\n")

# OUTPUT 2: The Navigation Map
print("OUTPUT 2: Navigation Map (*=Route, .=Safe, X=Obstacle)")
for r in range(ARENA_SIZE):
    row_str = []
    for c in range(ARENA_SIZE):
        if (r, c) in (route if route else []): row_str.append("*")
        elif arena[r][c] == 0: row_str.append("X")
        else: row_str.append(".")
    print(" ".join(row_str))