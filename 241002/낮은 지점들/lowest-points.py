import sys
from collections import defaultdict

input = sys.stdin.readline

d = defaultdict(int)

n = int(input())

for _ in range(n):
    x, y = map(int, input().split())

    if x not in d:
        d[x] = y
    else:
        if d[x] > y:
            d[x] = y

answer = 0
for value in d.values():
    answer += value

print(answer)