import sys
from collections import defaultdict
input = sys.stdin.readline

d = defaultdict(int)

n, m = map(int, input().split())

for elem in list(map(int, input().split())):
    d[elem] += 1

for elem in list(map(int, input().split())):
    print(d[elem], end=' ')