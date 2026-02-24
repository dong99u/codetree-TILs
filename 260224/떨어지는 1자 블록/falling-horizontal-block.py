n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def move():
    r = 0

    while True:
        if any(grid[r + 1][k:k + m]):
            grid[r][k:k + m] = [1] * m
            break
        r += 1
            

k -= 1

move()

for row in grid:
    print(*row)
