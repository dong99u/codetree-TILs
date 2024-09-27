import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())

answer = 0
d = defaultdict(int)

for _ in range(n):
    color = input().rstrip()
    d[color] += 1

    answer = max(answer, d[color])

print(answer)