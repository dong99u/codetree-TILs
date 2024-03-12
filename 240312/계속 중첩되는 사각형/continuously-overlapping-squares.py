from enum import Enum


class Color(Enum):
    RED = 1
    BLUE = 2


n = int(input())

MAX_XY = 200
OFFSET = 100

grid = [[0] * MAX_XY for _ in range(MAX_XY)]

for i in range(n):
    x1, y1, x2, y2 = tuple(map(int, input().split()))

    x1, y1, x2, y2 = x1 + OFFSET, y1 + OFFSET, x2 + OFFSET, y2 + OFFSET

    if i % 2 == 0:
        for x in range(x1, x2):
            for y in range(y1, y2):

                grid[x][y] = Color.RED

    else:
        for x in range(x1, x2):
            for y in range(y1, y2):

                grid[x][y] = Color.BLUE

answer = 0
for x in range(MAX_XY):
    for y in range(MAX_XY):

        if grid[x][y] == Color.BLUE:
            answer += 1

print(answer)