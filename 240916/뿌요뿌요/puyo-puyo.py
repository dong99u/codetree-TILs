import sys
input = sys.stdin.readline

n = int(input())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [False] * n
    for _ in range(n)
]

# 상하좌우
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

block_count = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def is_same(next_x, next_y, curr_x, curr_y):
    if not in_range(next_x, next_y):
        return False

    if grid[next_x][next_y] != grid[curr_x][curr_y]:
        return False

    return True
def dfs(x, y):
    global count, block_count

    visited[x][y] = True
    count += 1

    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy

        if is_same(nx, ny, x, y) and visited[nx][ny] is False:
            dfs(nx, ny)

max_count = 0
for x in range(n):
    for y in range(n):
        count = 0
        if visited[x][y] is False:
            dfs(x, y)
            if count >= 2:
                block_count += 1
            max_count = max(max_count, count)



print(block_count, max_count)