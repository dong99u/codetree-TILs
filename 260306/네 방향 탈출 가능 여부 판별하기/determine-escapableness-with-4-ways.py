from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_move(x, y):
    if not in_range(x, y):
        return False
    if a[nx][ny] == 0:
        return False
    if visited[nx][ny]:
        return False

    return True

visited = [[False] * m for _ in range(n)]
visited[0][0] = True

q = deque([(0, 0)])

while q:
    x, y = q.popleft()

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if can_move(nx, ny):
            visited[nx][ny] = True
            q.append((nx, ny))

valid = 1 if visited[n - 1][m - 1] else 0

print(valid)