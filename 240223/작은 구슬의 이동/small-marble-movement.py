def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# n: 격자 크기, t: t초후 시간
n, t = map(int, input().split())

x, y, d = input().split()
x, y = int(x) - 1, int(y) - 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


mapper = {
    'U': 0,
    'R': 1,
    'D': 2,
    'L': 3
}

dir_num = mapper[d]

for _ in range(t):
    nx = x + dx[dir_num]
    ny = y + dy[dir_num]

    if not in_range(nx, ny):
        dir_num = (dir_num + 2) % 4
        continue

    x, y = nx, ny

print(x + 1, y + 1)