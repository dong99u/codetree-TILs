n = int(input())

arr = [0] * 100

for _ in range(n):
    x1, x2 = tuple(map(int, input().split()))

    for i in range(x1, x2 + 1):
        arr[i] += 1

print(max(arr))