import heapq

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
INF = float('inf')
graph = [[] for _ in range(n + 1)]

for u, v, w in edges:
    graph[v].append((u, w))

D = [INF] * (n + 1)
D[n] = 0
hq = [(0, n)]

while hq:
    dist, curr = heapq.heappop(hq)

    if D[curr] != dist:
        continue

    for nxt, weight in graph[curr]:
        if D[nxt] > dist + weight:
            D[nxt] = dist + weight
            heapq.heappush(hq, (dist + weight, nxt))

print(max(D[1:]))