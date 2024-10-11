import sys
import heapq

input = sys.stdin.readline

n = int(input().rstrip())

heap = list(map(lambda x: -int(x), input().split()))

heapq.heapify(heap)

while len(heap) > 1:
    a = -heapq.heappop(heap) # 가장 큰 수
    b = -heapq.heappop(heap) # 두 번째로 큰 수

    diff = a - b
    if diff != 0:
        heapq.heappush(heap, -diff)

if len(heap) == 1:
    print(-heapq.heappop(heap))
else:
    print(-1)