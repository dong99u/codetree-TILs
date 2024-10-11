import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())

nums = list(map(int, input().split()))

heap = []

for num in nums:
    heapq.heappush(heap, -num)

for _ in range(m):
    max_num = -heapq.heappop(heap)
    heapq.heappush(heap, -max_num + 1)

print(-heap[0])