import sys

input = sys.stdin.readline

n = int(input().rstrip())

nums = list(map(int, input().split()))

s = set(nums)

print(len(s))