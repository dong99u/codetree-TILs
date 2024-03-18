import sys
INT_MAX = sys.maxsize

n, s= map(int, input().split())

arr = list(map(int, input().split()))

diff = INT_MAX
answer = 0
for i in range(n):
    for j in range(i + 1, n):

        arr[i] = arr[j] = 0

        val = sum(arr)

        if abs(val - s) < diff:
            answer = diff = abs(val - s)
            


print(answer)