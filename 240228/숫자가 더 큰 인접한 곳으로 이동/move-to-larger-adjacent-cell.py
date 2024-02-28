import sys

# 입력
n, x, y = tuple(map(int, sys.stdin.readline().split()))
x -= 1
y -= 1

grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# dx, dy
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def move() -> bool:
    global x, y
    x

    curr_num = grid[x][y]

    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy

        if not in_range(nx, ny):
            continue

        if curr_num < grid[nx][ny]:
            print(curr_num, end=" ")
            x, y = nx, ny
            return True

    print(curr_num, end=" ")
    return False


while move():
    print("", end="")