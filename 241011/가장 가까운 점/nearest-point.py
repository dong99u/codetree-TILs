import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())

points = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

heap = []

for point in points:
    x, y = point
    heapq.heappush(heap, (abs(x) + abs(y), x, y))

for _ in range(m):
    min_point = heapq.heappop(heap)
    min_x = min_point[1] + 2
    min_y = min_point[2] + 2

    heapq.heappush(heap, (abs(min_x) + abs(min_y), min_x, min_y))

last_min_point = heapq.heappop(heap)

print(last_min_point[1], last_min_point[2])