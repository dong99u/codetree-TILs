import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [False] * n
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    if not in_range(x, y):
        return False

    if grid[x][y] == 1:
        return False

    if visited[x][y]:
        return False

    return True

count = 0

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

q = deque()
for _ in range(k):
    start_x, start_y = map(int, input().split())
    q.append((start_x - 1, start_y - 1))
    visited[start_x - 1][start_y - 1] = True
    count += 1

while q:
    curr_x, curr_y = q.popleft()

    if visited[curr_x][curr_y] == False:
        visited[curr_x][curr_y] = True
        count += 1

    for dx, dy in zip(dxs, dys):
        next_x, next_y = curr_x + dx, curr_y + dy

        if can_go(next_x, next_y):
            q.append((next_x, next_y))

print(count)