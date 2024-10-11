import sys
import heapq

input = sys.stdin.readline

n = int(input().rstrip())

heap = []

for _ in range(n):
    x = int(input().rstrip())
    if x == 0:
        print(heapq.heappop(heap) if heap else 0)
    else:
        heapq.heappush(heap, x)