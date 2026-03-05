from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    if not in_range(x, y): return False
    if visited[x][y]: return False
    if grid[x][y] == 1: return False
    return True

answer = 0
visited = [[False] * n for _ in range(n)]
points = [(x - 1, y - 1) for x, y in points]
q = deque(points)
for x, y in points:
    visited[x][y] = True
    answer += 1

while q:
    x, y = q.popleft()
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny):
            visited[nx][ny] = True
            q.append((nx, ny))
            answer += 1

print(answer)
