n, r, c = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

cx, cy = r - 1, c - 1

while True:
    print(a[cx][cy], end=' ')
    valid = False
    for dx, dy in zip(dxs, dys):
        nx, ny = cx + dx, cy + dy

        if not in_range(nx, ny):
            continue

        if a[cx][cy] < a[nx][ny]:
            cx, cy = nx, ny
            valid = True
            break

    if not valid:
        break


