import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [False] * m
    for _ in range(n)
]

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y):

    # 격자 밖이라면
    if not in_range(x, y):
        return False

    # 뱀이 있다면
    if grid[x][y] == 0:
        return False

    # 이미 방문한 곳이라면
    if visited[x][y]:
        return False

    return True


q = deque()
q.append((0, 0))

answer = 0
while q:
    curr_x, curr_y = q.popleft()

    if curr_x == n - 1 and curr_y == m - 1:
        answer = 1
        break

    for dx, dy in zip(dxs, dys):
        next_x = curr_x + dx
        next_y = curr_y + dy

        if can_go(next_x, next_y):
            visited[next_x][next_y] = True
            q.append((next_x, next_y))

print(answer)