n, m = map(int, input().split())

MAX_INT = float('inf')
coins = list(map(int, input().split()))

dp = [0] + [MAX_INT] * m

for i in range(1, m + 1):
    for j in range(n):
        if i >= coins[j]:
            if dp[i - coins[j]] == MAX_INT:
                continue

            dp[i] = min(dp[i], dp[i - coins[j]] + 1)

if dp[m] == float('inf'):
    print(-1)
else:
    print(dp[m])