from collections import deque

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c, m1, m2, m3, m4, dir = map(int, input().split())

# Please write your code here.

q = deque()

for i in range(m1 + 1):
    q.append(grid[r - 1 - i][c - 1 + i])

for i in range(m2):
    q.append(grid[r - 2 - m1 - i][c - 2 + m1 - i])

for i in range(m3):
    q.append(grid[r - m1 - m2 + i][c - 2 + m1 - m2 - i])

for i in range(m4 - 1):
    q.append(grid[r - m1 - m2 + m3 + i][r + m1 - m2 - m3 + i])

if dir == 0:
    q.rotate(1)
else:
    q.rotate(-1)

for i in range(m1 + 1):
    grid[r - 1 - i][c - 1 + i] = q.popleft()

for i in range(m2):
    grid[r - 2 - m1 - i][c - 2 + m1 - i] = q.popleft()

for i in range(m3):
    grid[r - m1 - m2 + i][c - 2 + m1 - m2 - i] = q.popleft()

for i in range(m4 - 1):
    grid[r - m1 - m2 + m3 + i][r + m1 - m2 - m3 + i] = q.popleft()

for row in grid:
    print(*row)