n, k = map(int, input().split())

arr = [0] + list(map(int, input().split()))

prefix_sum = [0] * (n + 1)

for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i]

answer = 0

for i in range(1, n + 1):
    for j in range(i, n + 1):
        if prefix_sum[j] - prefix_sum[i - 1] == k:
            answer += 1

print(answer)