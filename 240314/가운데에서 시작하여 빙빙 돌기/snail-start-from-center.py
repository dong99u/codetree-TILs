def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def already_filled(x, y):
    return grid[x][y]


def end(x, y):
    return not in_range(x, y)


def move(dir_num):
    global x, y

    dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]

    x += dx[dir_num]
    y += dy[dir_num]


n = int(input())
grid = [[0] * n for _ in range(n)]

x = y = n // 2
dir_num, distance = 0, 1
num = 1

while not end(x, y):
    for _ in range(distance):
        grid[x][y] = num
        num += 1

        move(dir_num)

    dir_num = (dir_num + 1) % 4

    if dir_num == 0 or dir_num == 2:
        distance += 1

for row in grid:
    print(*row)