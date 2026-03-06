from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# Please write your code here.
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

x, y = r - 1, c - 1

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs(x, y):
    visited = [[False] * n for _ in range(n)]
    q = deque([(x, y)])
    visited[x][y] = True
    start_num = grid[x][y]
    max_num = 0
    max_pos = (-1, -1)
    while q:
        cx, cy = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = cx + dx, cy + dy
            if not in_range(nx, ny): continue
            if start_num <= grid[nx][ny]: continue
            if visited[nx][ny]: continue
            q.append((nx, ny))
            visited[nx][ny] = True
            if max_num == grid[nx][ny]:
                if max_pos > (nx, ny):
                    max_pos = (nx, ny)
            elif max_num < grid[nx][ny]:
                max_num = grid[nx][ny]
                max_pos = (nx, ny)

    return max_pos

for _ in range(k):
    next_x, next_y = bfs(x, y)
    if next_x == x and next_y == y:
        break
    x, y = next_x, next_y

print(x + 1, y + 1)


