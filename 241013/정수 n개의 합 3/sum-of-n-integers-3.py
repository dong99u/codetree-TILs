n, k = map(int, input().split())

grid = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    grid[i][1:] = list(map(int, input().split()))

prefix_sum = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1] + grid[i][j]

answer = 0
for i in range(k, n + 1):
    for j in range(k, n + 1):
        answer = max(answer, prefix_sum[i][j] - prefix_sum[i - k][j] - prefix_sum[i][j - k] + prefix_sum[i - k][j - k])

print(answer)