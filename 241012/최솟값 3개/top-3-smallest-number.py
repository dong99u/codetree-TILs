import sys
import heapq

input = sys.stdin.readline

n = int(input().rstrip())

arr = list(map(int, input().split()))

heap = []

for i in range(n):
    heapq.heappush(heap, arr[i])
    if len(heap) < 3:
        print(-1)

    else:
        n1 = heapq.heappop(heap)
        n2 = heapq.heappop(heap)
        n3 = heapq.heappop(heap)

        print(n1 * n2 * n3)

        heapq.heappush(heap, n1)
        heapq.heappush(heap, n2)
        heapq.heappush(heap, n3)