import heapq

n = int(input())

heap = []

for _ in range(n):
    order = input()

    if order.startswith('push'):
        num = int(order.split()[1])
        heapq.heappush(heap, -num)
    elif order.startswith('pop'):
        print(-heapq.heappop(heap))
    elif order.startswith('size'):
        print(len(heap))
    elif order.startswith('empty'):
        print(0 if heap else 1)
    elif order.startswith('top'):
        print(-heap[0])