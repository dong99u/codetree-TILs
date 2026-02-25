n, m, r, c = map(int, input().split())

# Please write your code here.
grid = [
    [0] * n
    for _ in range(n)
]

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

grid[r - 1][c - 1] = 1

for t in range(1, m + 1):
    dist = 2 ** (t - 1)
    temp = [grid[i][:] for i in range(n)]
    for x in range(n):
        for y in range(n):
            if grid[x][y] == 0:
                continue

            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx * dist, y + dy * dist

                if not in_range(nx, ny):
                    continue

                temp[nx][ny] = 1
    grid = [temp[i][:] for i in range(n)]

answer = 0
for i in range(n):
    for j in range(n):
        answer += grid[i][j]

print(answer)