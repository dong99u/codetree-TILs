import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

n, k, u, d = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(curr_x, curr_y, next_x, next_y):
    if not in_range(next_x, next_y):
        return False

    if visited[next_x][next_y]:
        return False

    diff = abs(grid[next_x][next_y] - grid[curr_x][curr_y])

    if not u <= diff <= d:
        return False

    return True

max_count = 0

positions = [(x, y) for x in range(n) for y in range(n)]

for selected_positions in combinations(positions, k):
    q = deque()
    visited = [
        [False] * n
        for _ in range(n)
    ]
    count = 0

    # Initialize queue and visited grid with starting positions
    for x, y in selected_positions:
        q.append((x, y))
        visited[x][y] = True  # Mark starting positions as visited
        count += 1  # Starting positions are counted

    while q:
        curr_x, curr_y = q.popleft()

        for dx, dy in zip(dxs, dys):
            next_x, next_y = curr_x + dx, curr_y + dy

            if can_go(curr_x, curr_y, next_x, next_y):
                visited[next_x][next_y] = True
                count += 1
                q.append((next_x, next_y))
    max_count = max(max_count, count)

print(max_count)