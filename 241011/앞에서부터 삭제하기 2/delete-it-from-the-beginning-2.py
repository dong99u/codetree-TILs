import sys
import heapq

input = sys.stdin.readline

n = int(input().rstrip())

nums = list(map(int, input().split()))

answer = 0

for k in range(1, n - 2 + 1):
    heap = nums[k:]
    heapq.heapify(heap)

    heapq.heappop(heap) # 가장 작은 수 하나를 뺌

    avg = round(sum(heap) / len(heap), 2)
    answer = max(answer, avg)

print(f'{answer:.2f}')