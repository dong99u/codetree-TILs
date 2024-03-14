# start_number와 격자의 n이 주어지면
# 시작위치와 방향(dir_num)을 return 하는 함수
# return (x, y, dir_num)
def initialize(start_num, n):

    if start_num <= n:
        return 0, start_num - 1, 0
    elif start_num <= 2 * n:
        return (start_num - 1) % n, n - 1, 1
    elif start_num <= 3 * n:
        return n - 1, (-start_num) % n, 2
    else:
        return (-start_num) % n, 0, 3

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def simulate(x, y, dir_num):
    move_num = 0
    while in_range(x, y):
        if grid[x][y] == '/':
            x, y, dir_num = move(x, y, dir_num ^ 1)
        else:
            x, y, dir_num = move(x, y, 3 - dir_num)

        move_num += 1

    return move_num

def move(x, y, next_dir):
    dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]
    nx, ny = x + dxs[next_dir], y + dys[next_dir]
    return nx, ny, next_dir

n = int(input())

grid = [
    list(input())
    for _ in range(n)
]

start_num = int(input())


x, y, dir_num = initialize(start_num, n)

move_num = simulate(x, y, dir_num)

print(move_num)