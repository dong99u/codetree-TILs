import sys

input = sys.stdin.readline

n, k = map(int, input().split())

arr = [0] + list(map(int, input().split()))
prefix_sum = [0] * (n + 1)
prefix_sum[1] = arr[1]

for i in range(1, n):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i]

max_num = 0

for i in range(k + 1, n):
    num = prefix_sum[i] - prefix_sum[i - k]
    max_num = max(max_num, num)

print(max_num)