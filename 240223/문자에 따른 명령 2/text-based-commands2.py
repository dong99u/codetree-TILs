instructions = input()

x, y = 0, 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

dir_num = 0

for instruction in instructions:
    if instruction == "R":
        dir_num = (dir_num + 1) % 4
    if instruction == "L":
        dir_num = (dir_num - 1 + 4) % 4

    if instruction == "F":
        nx = x + dx[dir_num]
        ny = y + dy[dir_num]

        x, y = nx, ny

print(x, y)