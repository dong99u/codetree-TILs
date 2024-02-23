# 움직이려는 거리
N = int(input())

# 시작 위치
x, y = 0, 0

# 동, 남, 서, 북 순서
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

directions = {
    'E': 0,
    'S': 1,
    'W': 2,
    'N': 3
}

for _ in range(N):
    direction, distance = tuple(input().split())
    direction = directions[direction]
    distance = int(distance)

    
    nx = x + dx[direction] * distance
    ny = y + dy[direction] * distance

    x = nx
    y = ny

print(x, y)