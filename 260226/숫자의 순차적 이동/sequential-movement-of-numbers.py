n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dxs = [1, 1, 0, -1, -1, -1, 0, 1]
dys = [0, 1, 1, 1, 0, -1, -1, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def move(num):
    for x in range(n):
        for y in range(n):
            if num == grid[x][y]:
                max_val = 0
                max_coord = (0, 0)
                for dx, dy in zip(dxs, dys):
                    nx, ny = x + dx, y + dy

                    if not in_range(nx, ny):
                        continue

                    if max_val < grid[nx][ny]:
                        max_val = grid[nx][ny]
                        max_coord = (nx, ny)

                nx, ny = max_coord
                grid[x][y], grid[nx][ny] = grid[nx][ny], grid[x][y]
                return


for _ in range(m):
    for num in range(1, n * n + 1):
        move(num)

for row in grid:
    print(*row)