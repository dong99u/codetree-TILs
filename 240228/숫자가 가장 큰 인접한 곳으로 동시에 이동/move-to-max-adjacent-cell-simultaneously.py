import sys


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def move(x, y):
    max_num, max_x, max_y = 0, -1, -1

    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy

        if not in_range(nx, ny):
            continue

        if max_num < grid[nx][ny]:
            max_num = grid[nx][ny]
            max_x, max_y = nx, ny

    next_ball_count[max_x][max_y] += 1


def check_crush():
    for row in range(n):
        for col in range(n):

            if next_ball_count[row][col] > 1:
                next_ball_count[row][col] == 0


# 입력
n, m, t = tuple(map(int, sys.stdin.readline().split()))

grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 구슬의 개수를 저장하는 격자
ball_count = [[0] * n for _ in range(n)]

for _ in range(m):
    x, y = tuple(map(int, sys.stdin.readline().split()))
    x -= 1
    y -= 1

    ball_count[x][y] = 1

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

for _ in range(t):
    next_ball_count = [[0] * n for _ in range(n)]

    for x in range(n):
        for y in range(n):

            # 구슬이 있다면
            # 구슬의 위치: (x, y)
            if ball_count[x][y] == 1:
                move(x, y)

    check_crush()
    ball_count = next_ball_count


count = 0
for i in range(n):
    for j in range(n):

        if ball_count[i][j] == 1:
            count += 1

print(count)