n = int(input())
num = [list(map(int, input().split())) for _ in range(n)]
move_dir = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# Please write your code here.
dxs = [-1, -1, 0, 1, 1, 1, 0, -1]
dys = [0, 1, 1, 1, 0, -1, -1, -1]

x, y = r - 1, c - 1

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def backtrack(x, y):
    result = 0
    d = move_dir[x][y] - 1
    nx, ny = x + dxs[d], y + dys[d]
    while in_range(nx, ny):
        if num[nx][ny] > num[x][y]:
            result = max(result, 1 + backtrack(nx, ny))
        nx += dxs[d]
        ny += dys[d]
    return result

answer = backtrack(x, y)

print(answer)