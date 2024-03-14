import sys

input = sys.stdin.readline

r, c = tuple(map(int, input().split()))

grid = [list(input().split()) for _ in range(r)]
answer = 0
if grid[0][0] == grid[r - 1][c - 1]:
    print(0)
else:
    for x1 in range(1, r - 2):
        for y1 in range(1, c - 2):

            if grid[x1][y1] != grid[0][0]:

                for x2 in range(x1 + 1, r - 1):
                    for y2 in range(y1 + 1, c - 1):
                        if grid[x2][y2] != grid[x1][y1]:
                            answer += 1

    print(answer)