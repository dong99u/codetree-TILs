def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


# 입력
n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]

temp = [[0] * n for _ in range(n)]

# 터지게 될 위치 (행, 열)
x, y = tuple(map(int, input().split()))


# x, y: 터지는 위치 (행,열), k: 범위
def bomb(x, y):
    global grid

    x = x - 1
    y = y - 1

    # 터지는 범위
    k = grid[x][y]

    for row in range(x - k + 1, x + k):
        if in_range(row, y):
            grid[row][y] = 0

    for col in range(y - k + 1, y + k):
        if in_range(x, col):
            grid[x][col] = 0


# 터짐
bomb(x, y)

for col in range(n):
    pointer = n - 1
    for row in range(n - 1, -1, -1):
        num = grid[row][col]

        if num != 0:
            temp[pointer][col] = num
            pointer -= 1


grid = temp

for elem in grid:
    print(*elem)