import sys
import heapq

input = sys.stdin.readline

n = int(input().rstrip())

arr = list(map(int, input().split()))

heap = []
answer = 0
heapq.heappush(heap, arr[-1])
for i in range(n - 2, 0, -1):
    heapq.heappush(heap, arr[i])
    others_without_min_val = heap[1:]
    avg = round(sum(others_without_min_val) / len(others_without_min_val), 2)

    answer = max(answer, avg)

print(f'{answer:.2f}')