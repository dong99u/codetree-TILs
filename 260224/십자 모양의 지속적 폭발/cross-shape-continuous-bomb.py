n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
commands = [int(input()) for _ in range(m)]

# Please write your code here.

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bomb(x, y):
    size = grid[x][y]

    grid[x][y] = 0

    for dx, dy in zip(dxs, dys):
        for i in range(size):
            nx, ny = x + dx * i, y + dy * i

            if not in_range(nx, ny):
                continue
            
            grid[nx][ny] = 0

    down()

def down():
    for j, col in enumerate(zip(*grid)):
        temp = []
        for num in col:
            if num != 0:
                temp.append(num)

        temp = [0] * (n - len(temp)) + temp

        for i in range(n - 1, -1, -1):
            grid[i][j] = temp[i]


for j in commands:
    j -= 1 # 0 indexed
    for i in range(n):
        if grid[i][j] == 0:
            continue

        bomb(i, j)
        down()
        break

for row in grid:
    print(*row)