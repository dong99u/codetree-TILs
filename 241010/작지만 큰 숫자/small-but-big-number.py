import sys
from sortedcontainers import SortedSet

input = sys.stdin.readline

n, m = map(int, input().split())

s = SortedSet(list(map(int, input().split())))

arr = list(map(int, input().split()))
for num in arr:

    idx = s.bisect_right(num)
    if idx != 0:
        print(s[idx - 1])
        s.pop(idx - 1)
    else:
        print(-1)