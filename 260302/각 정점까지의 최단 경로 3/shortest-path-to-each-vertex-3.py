import heapq

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
INF = float('inf')

graph = [[] for _ in range(n + 1)]

for u, v, w in edges:
    graph[u].append((v, w))

D = [INF] * (n + 1)
D[1] = 0
hq = [(0, 1)]

while hq:
    dist, curr = heapq.heappop(hq)

    for nxt, weight in graph[curr]:
        if D[nxt] > dist + weight:
            D[nxt] = dist + weight
            heapq.heappush(hq, (dist + weight, nxt))

for i in range(2, n + 1):
    print(D[i] if D[i] != INF else -1)