def make_square(x1, y1, x2, y2, value):
    global grid

    for x in range(x1 + OFFSET, x2 + OFFSET):
        for y in range(y1 + OFFSET, y2 + OFFSET):

            grid[x][y] = value


MAX_XY = 2000
OFFSET = 1000

grid = [[0] * MAX_XY for _ in range(MAX_XY)]


make_square(*tuple(map(int, input().split())), 1)
make_square(*tuple(map(int, input().split())), 0)

min_x, min_y, max_x, max_y = MAX_XY, MAX_XY, -1, -1

for x in range(MAX_XY):
    for y in range(MAX_XY):

        if grid[x][y] == 1:
            min_x = min(min_x, x)
            min_y = min(min_y, y)

            max_x = max(max_x, x)
            max_y = max(max_y, y)

if max_x == -1:
    print(0)
else:

    width = max_y - min_y + 1
    height = max_x - min_x + 1

    print(width * height)