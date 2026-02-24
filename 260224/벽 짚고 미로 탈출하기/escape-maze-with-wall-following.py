n = int(input())
sx, sy = map(int, input().split())

grid = [
    list(input())
    for _ in range(n)
]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

cx, cy = sx - 1, sy - 1
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]
dir_idx = 0
time = 0

visited = [
    [False] * n
    for _ in range(n)
]

valid = True
while in_range(cx, cy):
    if visited[cx][cy]:
        valid = False
        break

    visited[cx][cy] = True

    nx, ny = cx + dxs[dir_idx], cy + dys[dir_idx]

    if not in_range(nx, ny):
        time += 1
        break

    if grid[nx][ny] == '#':
        dir_idx = (dir_idx + 3) % 4
        nx, ny = cx + dxs[dir_idx], cy + dys[dir_idx]

        if grid[nx][ny] == '#':
            valid = False

    else:
        next_dir_idx = (dir_idx + 1) % 4
        if grid[nx + dxs[next_dir_idx]][ny + dys[next_dir_idx]] == '.':
            dir_idx = next_dir_idx

    cx, cy = nx, ny
    time += 1

print(time if valid else -1)
