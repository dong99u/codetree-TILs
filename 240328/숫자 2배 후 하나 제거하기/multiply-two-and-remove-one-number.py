n = int(input())

arr = list(map(int, input().split()))
answer = float("inf")
for i in range(n):
    temp = arr[i]
    arr[i] *= 2

    for j in range(n):
        remained = []
        for k in range(n):

            if j == k:
                continue

            remained.append(arr[k])
        sum_val = 0
        for l in range(1, n - 1):
            sum_val += abs(remained[l] - remained[l - 1])

        answer = min(answer, sum_val)

    arr[i] = temp

print(answer)