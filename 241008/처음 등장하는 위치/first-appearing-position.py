from sortedcontainers import SortedDict
import sys

n = int(input())
nums = list(map(int, input().split()))

sd = SortedDict()

for idx, num in enumerate(nums):
    if num not in sd:
        sd[num] = idx + 1

for key, val in sd.items():
    print(key, val)