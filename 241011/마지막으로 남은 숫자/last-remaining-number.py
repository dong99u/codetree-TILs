import sys
import heapq

input = sys.stdin.readline

n = int(input().rstrip())

heap = list(map(lambda x: -int(x), input().split()))

heapq.heapify(heap)

while len(heap) > 1:
    a = heapq.heappop(heap) # 가장 큰 수
    b = heapq.heappop(heap) # 두 번째로 큰 수

    heapq.heappush(heap, a - b)

print(-heap[0])