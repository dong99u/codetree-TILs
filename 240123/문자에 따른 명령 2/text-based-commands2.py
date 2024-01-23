x, y = 0, 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

dir_num = 0

user_input = input()

for elem in user_input:
    if elem == 'L':
        dir_num = (dir_num + 3) % 4
    elif elem == 'R':
        dir_num = (dir_num + 1) % 4
    elif elem == 'F':
        nx = x + dx[dir_num]
        ny = y + dy[dir_num]

        x, y = nx, ny

print(x, y)