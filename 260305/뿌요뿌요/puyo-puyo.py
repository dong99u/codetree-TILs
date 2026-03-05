n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

visited = [[False] * n for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def dfs(x, y):
    visited[x][y] = True
    result = 1
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if not in_range(nx, ny):
            continue
        if visited[nx][ny]:
            continue
        if grid[nx][ny] == grid[x][y]:
            result += dfs(nx, ny)

    return result

max_count = 0
count = 0
for x in range(n):
    for y in range(n):
        if not visited[x][y]:
            result = dfs(x, y)
            if result >= 4:
                count += 1

            if max_count < result:
                max_count = result

print(count, max_count)
