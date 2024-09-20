import sys
input = sys.stdin.readline

n = int(input())
arr = []

dp = [0] * n

for _ in range(n):
    arr.append(tuple(map(int, input().split())))

for i in range(n):
    s1, e1, p1 = arr[i]

    dp[i] = max(dp[i], dp[i] + p1)

    for j in range(i, n):
        s2, e2, p2 = arr[j]

        if e1 < s2:
            dp[i] = max(dp[i], dp[i] + p2)

print(max(dp))