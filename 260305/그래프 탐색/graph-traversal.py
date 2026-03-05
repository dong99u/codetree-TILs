n, m = map(int, input().split())

# Please write your code here.
visited = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(v):
    result = 0
    visited[v] = True
    for nxt in graph[v]:
        if not visited[nxt]:
            result += dfs(nxt) + 1

    return result

answer = dfs(1)

print(answer)

