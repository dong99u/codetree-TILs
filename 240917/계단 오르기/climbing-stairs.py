n = int(input())

dp = [0] * (n + 2)

dp[2] = 1
dp[3] = 1

for i in range(4, n + 1):
    dp[i] = dp[i - 2] + dp[i - 3]

if dp[n] == 0:
    print(0)
else:
    print(dp[n] % 10007)