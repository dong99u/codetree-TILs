import sys

input = sys.stdin.readline

n, k = map(int, input().split())

swaps = []
# 입력값 받기
for _ in range(k):
    swaps.append(tuple(map(int, input().split())))

counts = [set([i]) for i in range(1, n + 1)]
nums = [
    i for i in range(1, n + 1)
]

for _ in range(3):
    for swap in swaps:
        a, b = swap
        a -= 1
        b -= 1
        nums[a], nums[b] = nums[b], nums[a]
        counts[nums[a] - 1].add(a + 1)
        counts[nums[b] - 1].add(b + 1)


for count in counts:
    print(len(count))