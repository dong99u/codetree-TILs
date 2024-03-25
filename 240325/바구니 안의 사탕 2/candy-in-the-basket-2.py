n, k = map(int, input().split())
MAX = 100
arr = [0] * (MAX + 1)

for _ in range(n):
    candy, pos = map(int, input().split())
    arr[pos] += candy


answer = 0
for i in range(MAX):

    sum_all = 0
    for j in range(i - k, i + 1 + 1):
        if j >= 0 and j <= MAX:
            sum_all += arr[j]

    answer = max(sum_all, answer)

print(answer)