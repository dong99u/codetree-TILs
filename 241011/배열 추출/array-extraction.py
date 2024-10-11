import sys
import heapq

input = sys.stdin.readline

n = int(input().rstrip())

heap = []

for _ in range(n):
    num = int(input().rstrip())

    if num == 0:
        print(-heapq.heappop(heap) if heap else 0)
    else:
        heapq.heappush(heap, -num)