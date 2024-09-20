import sys
input = sys.stdin.readline
MIN_INT = -sys.maxsize

n = int(input())

arr = list(map(int, input().split()))

dp = [MIN_INT] * n
dp[0] = 0

for i in range(1, n):
    for j in range(i):
        if dp[j] == MIN_INT:
            continue

        if j + arr[j] >= i:
            dp[i] = max(dp[j] + 1, dp[i])



print(max(dp))