MAX_XY = 200
OFFSET = 100

n = int(input())

grid = [
    [0] * MAX_XY
    for _ in range(MAX_XY)
]

for _ in range(n):

    x1, y1 = tuple(map(int, input().split()))

    for x in range(x1 + OFFSET, x1 + OFFSET + 8):
        for y in range(y1 + OFFSET, y1 + OFFSET + 8):
            grid[x][y] = 1

answer = 0

for x in range(MAX_XY):
    for y in range(MAX_XY):

        if grid[x][y] == 1:
            answer += 1

print(answer)