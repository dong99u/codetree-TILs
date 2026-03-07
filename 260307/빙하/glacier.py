from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs():
    visited = [[False] * m for _ in range(n)]
    q = deque([(0, 0)])
    visited[0][0] = True
    count = 0
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if not in_range(nx, ny):
                continue
            if visited[nx][ny]:
                continue
            if a[nx][ny] == 0:
                q.append((nx, ny))
            elif a[nx][ny] == 1:
                a[nx][ny] = 0
                count += 1
            visited[nx][ny] = True

    return count

time = 0
answer_count = 0
while True:
    count = bfs()
    if count == 0:
        break
    answer_count = count
    time += 1

print(time, answer_count)