n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dxs = [1, 0]
dys = [0, 1]
visited = [[False] * m for _ in range(n)]
visited[0][0] = True

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def dfs(x, y):
    if x == n - 1 and y == m - 1:
        return 1

    result = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if not in_range(nx, ny):
            continue
        if grid[nx][ny] == 0:
            continue
        if visited[nx][ny]:
            continue
        visited[nx][ny] = True
        result = dfs(nx, ny)
        if result:
            return result

    return result

answer = dfs(0, 0)

print(answer)


