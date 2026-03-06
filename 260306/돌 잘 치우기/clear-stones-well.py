from collections import deque

n, k, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

start_pos = []
for _ in range(k):
    ri, ci = map(int, input().split())
    start_pos.append((ri - 1, ci - 1))

# Please write your code here.
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def backtrack(idx, count):
    '''
    idx: idx 부터 지울 돌을 고름
    count: 현재까지 고른 치울 돌의 개수
    max_count: 방문 가능한 서로 다른 칸의 개수
    '''
    if idx == rock_count:
        if count != m: return 0
    if count == m: return bfs()

    result = 0
    for i in range(idx, rock_count):
        selected_rocks.append(i)
        result = max(result, backtrack(i + 1, count + 1))
        selected_rocks.pop()

    return result

def remove_rocks():
    for i in selected_rocks:
        x, y = rock_pos[i]
        grid[x][y] = 0

def rollback_rocks():
    for i in selected_rocks:
        x, y = rock_pos[i]
        grid[x][y] = 1

def bfs():
    remove_rocks()
    visited = [[False] * n for _ in range(n)]
    q = deque(start_pos)
    for x, y in start_pos:
        visited[x][y] = True
    count = len(start_pos)
    while q:
        cx, cy = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = cx + dx, cy + dy
            if not in_range(nx, ny): continue
            if visited[nx][ny]: continue
            if grid[nx][ny] == 1: continue
            q.append((nx, ny))
            visited[nx][ny] = True
            count += 1
    rollback_rocks()
    return count

rock_pos = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            rock_pos.append((i, j))

rock_count = len(rock_pos)
selected_rocks = []
answer = backtrack(0, 0)

print(answer)