import sys
input = sys.stdin.readline

n, m = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

dxs = [1, 0]
dys = [0, 1]

visited = [
    [False] * m
    for _ in range(n)
]

def can_go(x, y):
    # 격자 밖인 경우
    if not 0 <= x < n or not 0 <= y < m:
        return False

    # 뱀이 있는 경우
    if grid[x][y] == 0:
        return False

    # 방문한 적이 없는 경우
    if visited[x][y]:
        return False

    return True

answer = 0
def dfs(x, y):
    global answer
    if x == n - 1 and y == m - 1:
        answer = 1
        return


    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy

        if can_go(nx, ny):
            visited[nx][ny] = True
            dfs(nx, ny)


visited[0][0] = True

dfs(0, 0)

print(answer)