OFFSET = 100

n = int(input())

arr = [0] * (200 - 1)
for _ in range(n):
    x1, x2 = tuple(map(int, input().split()))
    x1, x2 = x1 + OFFSET, x2 + OFFSET

    for i in range(x1, x2):
        arr[i] += 1

    
print(max(arr))