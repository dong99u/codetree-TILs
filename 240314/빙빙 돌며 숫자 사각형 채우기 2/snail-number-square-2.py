n, m = tuple(map(int, input().split()))

grid = [[0] * m for _ in range(n)]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def already_filled(x, y):
    return grid[x][y] != 0


def simulate():
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    # 시작 위치
    x, y = 0, 0
    # 시작 방향
    dir_num = 0

    for num in range(1, n * m + 1):
        grid[x][y] = num
        nx, ny = x + dx[dir_num], y + dy[dir_num]

        if not in_range(nx, ny) or already_filled(nx, ny):
            dir_num = (dir_num + 1) % 4
            nx, ny = x + dx[dir_num], y + dy[dir_num]

        x, y = nx, ny


simulate()

for row in grid:
    print(*row)