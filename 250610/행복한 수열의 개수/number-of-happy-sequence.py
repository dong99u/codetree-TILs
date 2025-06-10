n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
answer = 0

for x in range(n):
    cnt, max_cnt = 1, 1
    for i in range(1, len(grid[x])):
        if grid[x][i - 1] == grid[x][i]:
            cnt += 1
        else:
            cnt = 1
        max_cnt = max(max_cnt, cnt)

    if max_cnt >= m:
        answer += 1

for y in range(n):
    cnt, max_cnt = 1, 1
    for i in range(1, len(grid)):
        if grid[i - 1][y] == grid[i][y]:
            cnt += 1
        else:
            cnt = 1
        max_cnt = max(max_cnt, cnt)
    
    if max_cnt >= m:
        answer += 1

print(answer)
