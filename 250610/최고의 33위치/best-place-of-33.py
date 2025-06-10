n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
answer = 0
for x in range(n):
    for y in range(n):
        cnt = 0
        if x + 3 > n or y + 3 > n:
            continue
        for i in range(3):
            for j in range(3):
                cnt += grid[x + i][y + j]
        
        answer = max(answer, cnt)

print(answer)