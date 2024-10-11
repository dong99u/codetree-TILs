import sys
import heapq

input = sys.stdin.readline

n = int(input().rstrip())

arr = list(map(int, input().split()))

heap = []
answer = 0
heapq.heappush(heap, arr[-1])

sum_val = arr[-1]

for i in range(n - 2, 0, -1):
    heapq.heappush(heap, arr[i])
    sum_val += arr[i]

    min_val = heap[0]
    avg = round((sum_val - min_val) / (len(heap) - 1), 2)

    answer = max(answer, avg)

print(f'{answer:.2f}')