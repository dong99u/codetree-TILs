import sys
from enum import Enum


def in_range(x, y):
    return 0 <= x < MAX_XY and 0 <= y < MAX_XY


class Color(Enum):
    BLACK = 1
    WHITE = 2


input = sys.stdin.readline

MAX_XY = 19

grid = [list(map(int, input().split())) for _ in range(MAX_XY)]

answer = 0
dxs, dys = [0, 1, 1, 1, 0, -1, -1, -1], [1, 1, 0, -1, -1, -1, 0, 1]
for i in range(MAX_XY):
    for j in range(MAX_XY):

        if grid[i][j] == 0:
            continue

        color = Color.BLACK if grid[i][j] == 1 else Color.WHITE

        for dx, dy in zip(dxs, dys):
            cnt = 1
            curr_x = i
            curr_y = j

            while True:
                nx = curr_x + dx
                ny = curr_y + dy
                if not in_range(nx, ny):
                    break
                if grid[nx][ny] != color.value:
                    break

                cnt += 1
                curr_x, curr_y = nx, ny

            if cnt == 5:
                print(color.value)
                print(i + 2 * dx + 1, j + 2 * dy + 1)
                sys.exit()

print(0)