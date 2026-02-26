n, m, t = map(int, input().split())

# Create n x n grid
a = [list(map(int, input().split())) for _ in range(n)]

# Get m marble positions

current = [
    [0] * n
    for _ in range(n)
]


for _ in range(m):
    r, c = map(int, input().split())
    current[r - 1][c - 1] = 1

# Please write your code here.
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def move():
    global current

    nxt = [
        [0] * n
        for _ in range(n)
    ]

    for x in range(n):
        for y in range(n):
            if current[x][y] != 1:
                continue

            nxt_max_val = 0
            mx, my = 0, 0

            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy

                if not in_range(nx, ny):
                    continue

                if a[nx][ny] > nxt_max_val:
                    nxt_max_val = a[nx][ny]
                    mx, my = nx, ny

            nxt[mx][my] += 1

    for x in range(n):
        for y in range(n):
            if nxt[x][y] > 1:
                nxt[x][y] = 0

    current = nxt

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]


for _ in range(t):
    move()

answer = 0
for i in range(n):
    for j in range(n):
        answer += current[i][j]

print(answer)