import sys

input = sys.stdin.readline

n, t = tuple(map(int, input().split()))

sequence = tuple(map(int, input().split()))

cnt = 0
answer = 0

for i in range(n):

    if i == 0 and t < sequence[i]:
        cnt += 1

    elif i >= 1 and t < sequence[i]:
        cnt += 1

    else:
        cnt = 0

    answer = max(answer, cnt)

print(answer)