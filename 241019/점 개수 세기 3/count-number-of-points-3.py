import sys
from sortedcontainers import SortedSet

input = sys.stdin.readline

n, q = map(int, input().split())

nums = list(map(int, input().split()))

queries = [
    list(map(int, input().split())) for _ in range(q)
    ]

nums_set = SortedSet(nums)

nums_dict = dict()

for idx, num in enumerate(nums_set):
    nums_dict[idx] = num

for query in queries:
    l, r = query

    l_idx = nums_set.bisect_left(l)
    r_idx = nums_set.bisect_right(r)

    print(r_idx - l_idx)