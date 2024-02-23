def is_home(x, y):
    return x == 0 and y == 0

instructions = input()

# (x, y): 현재 위치
x, y = 0, 0
counter = 0

# 북, 동, 남, 서 순서
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

dir_num = 0

for instruction in instructions:
    if instruction == 'R':
        dir_num = (dir_num + 1) % 4
    if instruction == 'L':
        dir_num = (dir_num + 4 - 1) % 4
    if instruction == 'F':
        x += dx[dir_num]
        y += dy[dir_num]

    counter += 1

    if is_home(x, y):
        break

if is_home(x, y):
    print(counter)
else: 
    print(-1)