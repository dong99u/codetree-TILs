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

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):

    if not in_range(x, y):
        return False

    if grid[x][y] == 0:
        return False

    if visited[x][y]:
        return False

    return True

total_village_count = 0
results = []

def dfs(x, y):
    global count

    visited[x][y] = True
    count += 1

    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy

        if can_go(nx, ny):
            dfs(nx, ny)


for x in range(n):
    for y in range(n):

        if not visited[x][y] and grid[x][y] != 0:
            count = 0
            dfs(x, y)
            total_village_count += 1
            results.append(count)


results.sort()
print(total_village_count)
for result in results:
    print(result)