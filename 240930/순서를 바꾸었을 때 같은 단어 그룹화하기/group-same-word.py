import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())

d = defaultdict(int)

answer = 0
for _ in range(n):
    word = input().rstrip()
    word = sorted(word)
    word = "".join(word)
    d[word] += 1

    answer = max(answer, d[word])

print(answer)