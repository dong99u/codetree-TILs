import heapq

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
A, B = map(int, input().split())

# Please write your code here.

def dijkstra(source):
    hq = [(0, source)]

    while hq:
        curr_dist, curr = heapq.heappop(hq)

        if curr_dist != dist[curr]:
            continue

        for nxt, weight in graph[curr]:
            new_dist = curr_dist + weight
            if dist[nxt] > new_dist:
                dist[nxt] = new_dist
                path[nxt] = curr
                heapq.heappush(hq, (new_dist, nxt))


INF = float('inf')

graph = [[] for _ in range(n + 1)]
for u, v, w in edges:
    graph[u].append((v, w))
    graph[v].append((u, w))

dist = [INF] * (n + 1)
dist[A] = 0
path = [i for i in range(n + 1)]

dijkstra(A)

print(dist[B])
paths = []
x = B
while x != A:
    paths.append(x)
    x = path[x]

print(paths[::-1])


