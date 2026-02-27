T = int(input())

dxs = [1, 0, 0, -1]
dys = [0, -1, 1, 0]

mapper = {
    'D': 0,
    'L': 1,
    'R': 2,
    'U': 3,
}


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def move():
    nxt = [
        [[None, 0] for _ in range(n)]
        for _ in range(n)
    ]
    for x in range(n):
        for y in range(n):
            if current[x][y] is not None:
                d = current[x][y]
                nx, ny = x + dxs[d], y + dys[d]
                if not in_range(nx, ny):
                    # 방향 전환
                    nxt[x][y] = [3 - d, nxt[x][y][1] + 1]
                else:
                    nxt[nx][ny] = [current[x][y], nxt[nx][ny][1] + 1]

    for x in range(n):
        for y in range(n):
            if nxt[x][y][1] == 1:
                current[x][y] = nxt[x][y][0]
            elif nxt[x][y][1] == 0:
                current[x][y] = None
            elif nxt[x][y][1] > 1:
                current[x][y] = None


for _ in range(T):
    n, m = map(int, input().split())
    current = [
        [None] * n
        for _ in range(n)
    ]
    for _ in range(m):
        xi, yi, di = input().split()
        xi = int(xi) - 1
        yi = int(yi) - 1
        current[xi][yi] = mapper[di]

    for _ in range(2 * n - 1):
        move()

    answer = 0
    for x in range(n):
        for y in range(n):
            if current[x][y] is not None:
                answer += 1

    print(answer)