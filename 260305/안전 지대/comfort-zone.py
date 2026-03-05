from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

def bfs(x, y, visited):
    q = deque([(x, y)])
    visited[x][y] = True

    while q:
        cx, cy = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = cx + dx, cy + dy
            if not in_range(nx, ny): continue
            if visited[nx][ny]: continue
            if grid[nx][ny] <= k: continue
            visited[nx][ny] = True
            q.append((nx, ny))

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

max_height = 0
for i in range(n):
    for j in range(m):
        max_height = max(max_height, grid[i][j])

max_k = -1
max_count = -1
for k in range(1, max_height + 1):
    visited = [[False] * m for _ in range(n)]
    count = 0
    for x in range(n):
        for y in range(m):
            if not visited[x][y] and grid[x][y] > k:
                bfs(x, y, visited)
                count += 1
    if max_count < count:
        max_count = count
        max_k = k

print(max_k, max_count)