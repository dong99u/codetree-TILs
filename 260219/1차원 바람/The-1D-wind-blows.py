from collections import deque

n, m, q = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
winds = [(int(r), d) for r, d in [input().split() for _ in range(q)]]

# Please write your code here.
grid = []

for row in a:
    q = deque(row)
    grid.append(q)

for r, d in winds:
    curr = r - 1
    if d == 'R':
        grid[curr].rotate(-1)
    elif d == 'L':
        grid[curr].rotate(1)

    up = curr - 1
    down = curr + 1

    up_dir = 1 if d == 'R' else -1
    down_dir = 1 if d == 'R' else -1

    while up >= 0:
        valid = False
        for i in range(m):
            if grid[up][i] == grid[up + 1][i]:
                grid[up].rotate(up_dir)
                up -= 1
                up_dir *= -1
                valid = True
                break
        if not valid:
            break

    while down < n:
        valid = False
        for i in range(m):
            if grid[down][i] == grid[down - 1][i]:
                grid[down].rotate(down_dir)
                down += 1
                down_dir *= -1
                valid = True
                break
        if not valid:
            break

for row in grid:
    print(*row)