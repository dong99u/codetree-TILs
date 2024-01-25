def is_moved():
    global prev_x, prev_y

    return prev_x != x or prev_y != y


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def move():
    global x, y, prev_x, prev_y
    # 상하좌우 순서
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if not in_range(nx, ny):
            continue
        if grid[nx][ny] > grid[x][y]:
            path.append(grid[nx][ny])
            prev_x, prev_y = x, y
            x, y = nx, ny
            return

    prev_x, prev_y = x, y


n, x, y = map(int, input().split())  # n: 격자의 크기, (x, y): 시작 위치

x -= 1
y -= 1

prev_x, prev_y = -1, -1

grid = [list(map(int, input().split())) for _ in range(n)]

path = [grid[x][y]]  # 시작 위치 숫자 저장

while is_moved():
    move()

print(*path)