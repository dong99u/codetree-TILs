n, k = map(int, input().split())
MAX = 101
arr = [0] * MAX

for _ in range(n):
    candy, pos = map(int, input().split())
    arr[pos] = candy


answer = 0
for c in range(k, 100 - k + 1):

    candy_sum = sum(arr[c - k : c + k + 1])
    answer = max(candy_sum , answer)

print(answer)