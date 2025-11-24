n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def f(arr):
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i] = arr[i] // 2

f(arr)
print(*arr)