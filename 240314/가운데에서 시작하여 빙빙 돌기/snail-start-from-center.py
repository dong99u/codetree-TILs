def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def already_filled(x, y):
    return grid[x][y]


n = int(input())

# 시작 위치
x, y = n - 1, n - 1
dir_num = 0

grid = [
    [0] * n
    for _ in range(n)
]

dx, dy = [0, -1, 0, 1], [-1, 0, 1, 0]

for num in range(n * n, 0, -1):
    grid[x][y] = num

    nx, ny = x + dx[dir_num], y + dy[dir_num]

    if not in_range(nx, ny) or already_filled(nx, ny):
        dir_num = (dir_num + 1) % 4
        nx, ny = x + dx[dir_num], y + dy[dir_num]

    x, y = nx, ny

for row in grid:
    print(*row)