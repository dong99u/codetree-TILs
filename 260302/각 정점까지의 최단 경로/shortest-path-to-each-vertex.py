import heapq

n, m = map(int, input().split())
k = int(input())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
INF = float('inf')

graph = [[] for _ in range(n + 1)]

for u, v, w in edges:
    graph[u].append((v, w))
    graph[v].append((u, w))

D = [INF] * (n + 1)
D[k] = 0
hq = [(0, k)]

while hq:
    dist, curr = heapq.heappop(hq)

    if dist != D[curr]:
        continue

    for nxt, weight in graph[curr]:
        if D[nxt] > dist + weight:
            D[nxt] = dist + weight
            heapq.heappush(hq, (dist + weight, nxt))

for i in range(1, n + 1):
    print(D[i] if D[i] != INF else -1)