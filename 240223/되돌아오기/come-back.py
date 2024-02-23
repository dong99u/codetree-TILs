def is_home(x, y):
    return x == 0 and y == 0

N = int(input())

counter = 0

# (x, y): 위치
x, y = 0, 0

# 북, 동, 남, 서 순서
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

mapper = {
    'N': 0,
    'E': 1,
    'S': 2,
    'W': 3
}

for _ in range(N):
    direction, distance = input().split()
    dir_num = mapper[direction]
    distance = int(distance)

    for d in range(distance):
        x += dx[dir_num]
        y += dy[dir_num]
        counter += 1
        if is_home(x, y):
            break
    if is_home(x, y):
        break

if x == 0 and y == 0:
    print(counter)
else:
    print(-1)