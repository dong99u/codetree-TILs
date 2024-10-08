from sortedcontainers import SortedDict
import sys

input = sys.stdin.readline

n = int(input().rstrip())

sd = SortedDict()

for _ in range(n):
    word = input().rstrip()

    if word in sd:
        sd[word] += 1
    else:
        sd[word] = 1

for key, val in sd.items():
    print(key, val)