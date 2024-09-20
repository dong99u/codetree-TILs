n = int(input())
arr = []

for _ in range(n):
    arr.append(tuple(map(int, input().split())))

# Sort the jobs based on end times
arr.sort(key=lambda x: x[1])

dp = [0] * n

for i in range(n):
    s_i, e_i, p_i = arr[i]
    dp[i] = p_i  # Initialize with the payment of the current job
    for j in range(i):
        s_j, e_j, p_j = arr[j]
        if e_j < s_i:  # Non-overlapping condition
            dp[i] = max(dp[i], dp[j] + p_i)

print(max(dp))