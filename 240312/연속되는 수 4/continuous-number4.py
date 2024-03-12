import sys
input = sys.stdin.readline

n = int(input())

sequence = [int(input()) for _ in range(n)]

cnt = 1
answer = 1

for i in range(1, n):

    if sequence[i - 1] < sequence[i]:
        cnt += 1
    else:
        cnt = 1

    answer = max(answer, cnt)

print(answer)