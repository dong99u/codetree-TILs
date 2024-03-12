import sys

input = sys.stdin.readline


# 부호가 같으면 False, 다르면 True
def check(x, y):
    if (x < 0 and y < 0) or (x > 0 and y > 0):
        return False
    return True


n = int(input())

sequence = [int(input()) for _ in range(n)]

cnt = 1
answer = 1

for i in range(1, n):

    if check(sequence[i], sequence[i - 1]):
        cnt = 1
    else:
        cnt += 1

    answer = max(answer, cnt)

print(answer)