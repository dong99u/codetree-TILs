import sys
from sortedcontainers import SortedSet

input = sys.stdin.readline

n, m = map(int, input().split())

n_arr = list(map(int, input().split()))

s = SortedSet(n_arr)

for _ in range(m):
    num = int(input().rstrip())

    if s:
        idx = s.bisect_left(num)
        if idx == len(s):
            print(-1)
        else:
            print(s[idx])