n, m = tuple(map(int, input().split()))

grid = [
    [''] * m
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def already_filled(x, y):
    return grid[x][y]

def simulate():
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

    dir_num = 0
    x, y = 0, 0

    code = 65
    for _ in range(n * m):
        if code > 90: code = 65

        grid[x][y] = chr(code)

        nx, ny = x + dx[dir_num], y + dy[dir_num]

        if not in_range(nx, ny) or already_filled(nx, ny):
            dir_num = (dir_num + 1) % 4
            nx, ny = x + dx[dir_num], y + dy[dir_num]

        x, y = nx, ny

        code += 1


simulate()

for row in grid:
    print(*row)