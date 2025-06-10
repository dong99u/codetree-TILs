n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
answer = 0

for x in range(n):
    cnt = 1
    for i in range(1, len(grid[x])):
        if grid[x][i - 1] == grid[x][i]:
            cnt += 1
        else:
            cnt = 1
        if cnt >= m:
            answer += 1
            break

for y in range(n):
    cnt = 1
    for i in range(1, len(grid)):
        if grid[i - 1][y] == grid[i][y]:
            cnt += 1
        else:
            cnt = 1
        if cnt >= m:
            answer += 1
            break

print(answer)
