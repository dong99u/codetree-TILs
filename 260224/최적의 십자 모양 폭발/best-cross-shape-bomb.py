n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1],

def dfs(x, y, grid):
    grid = [row[:] for row in grid]
    grid = boom(x, y, grid)
    grid = drop(grid)
    count = check(grid)

    return count

def boom(x, y, grid):
    k = grid[x][y]
    grid[x][y] = 0
    for dx, dy in zip(dxs, dys):
        for i in range(k):
            nx, ny = x + dx * i, y + dy * i

            if not in_range(nx, ny):
                continue

            grid[nx][ny] = 0
    return grid

def drop(grid):
    for j in range(n):
        nums = [grid[i][j] for i in range(n) if grid[i][j] != 0]

        if not nums:
            continue

        nums = [0] * (n - len(nums)) + nums
        for i in range(n):
            grid[i][j] = nums[i]

    return grid

def check(grid):
    result = 0

    visited = [[False] * n for _ in range(n)]

    for cx in range(n):
        for cy in range(n):
            if grid[cx][cy] == 0: continue
            visited[cx][cy] = True
            for dx, dy in zip(dxs, dys):
                nx, ny = cx + dx, cy + dy

                if not in_range(nx, ny):
                    continue

                if visited[nx][ny]:
                    continue

                if grid[cx][cy] == grid[nx][ny]:
                    result += 1

    return result


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

answer = 0
for i in range(n):
    for j in range(n):
        answer = max(answer, dfs(i, j, grid))

print(answer)
