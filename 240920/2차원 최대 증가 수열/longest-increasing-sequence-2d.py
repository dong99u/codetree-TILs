import sys
input = sys.stdin.readline

MIN_INT = -sys.maxsize

n, m = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

dp = [
    [0] * m
    for _ in range(n)
]

dp[0][0] = 1

for x in range(1, n):
    for y in range(1, n):

        for i in range(x):
            for j in range(y):

                if dp[i][j] == 0:
                    continue

                if grid[x][y] > grid[i][j]:
                    dp[x][y] = max(dp[i][j] + 1, dp[x][y])
answer = MIN_INT
for row in dp:
    for num in row:
        if answer < num:
            answer = num

print(answer)