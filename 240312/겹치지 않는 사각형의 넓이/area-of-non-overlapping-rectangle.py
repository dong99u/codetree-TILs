MAX_XY = 2000

OFFSET = 1000

grid = [
    [0] * MAX_XY
    for _ in range(MAX_XY)
]

for _ in range(2):
    x1, y1, x2, y2 = tuple(map(int, input().split()))

    for x in range(x1 + OFFSET, x2 + OFFSET):
        for y in range(y1 + OFFSET, y2 + OFFSET):
            grid[x][y] = 1

    
x1, y1, x2, y2 = tuple(map(int, input().split()))

for x in range(x1 + OFFSET, x2 + OFFSET):
        for y in range(y1 + OFFSET, y2 + OFFSET):
            grid[x][y] = 0

answer = 0

for x in range(MAX_XY):
    for y in range(MAX_XY):
        if grid[x][y] == 1:
            answer += 1

print(answer)