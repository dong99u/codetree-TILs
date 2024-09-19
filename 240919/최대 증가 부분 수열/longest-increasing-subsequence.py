import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

dp = [0] * n
dp[0] = 1
for i in range(1, n):
    if arr[i - 1] < arr[i]:
        dp[i] = dp[i - 1] + 1
    else:
        dp[i] = dp[i - 1]


print(dp[-1])