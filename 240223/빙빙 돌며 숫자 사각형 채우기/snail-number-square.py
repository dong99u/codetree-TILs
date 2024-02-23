def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

n, m = map(int, input().split())
grid = [
    [0] * m
    for _ in range(n)
]

x, y = 0, 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

dir_num = 0

for i in range(1, n * m + 1):
    grid[x][y] = i

    nx = x + dx[dir_num]
    ny = y + dy[dir_num]

    if not in_range(nx, ny) or grid[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4
        nx = x + dx[dir_num]
        ny = y + dy[dir_num]

    x, y = nx, ny

for row in grid:
    print(*row)