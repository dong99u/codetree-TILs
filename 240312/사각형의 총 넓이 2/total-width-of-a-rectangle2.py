n = int(input())

MAX_X = 200
MAX_Y = 200

OFFSET = 100

grid = [
    [0] * MAX_X
    for _ in range(MAX_Y)
]

for _ in range(n):
    x1, y1, x2, y2 = tuple(map(int, input().split()))
    x1, y1, x2, y2 = x1 + OFFSET, y1 + OFFSET, x2 + OFFSET, y2 + OFFSET

    for x in range(x1, x2):
        for y in range(y1, y2):

            grid[x][y] = 1


answer = 0
for x in range(MAX_X):
    for y in range(MAX_Y):
        
        if grid[x][y] == 1:
            answer += 1

print(answer)