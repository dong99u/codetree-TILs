import sys
input = sys.stdin.readline

INF = float('inf')
n, m = map(int, input().split())

graph = [
    [] for _ in range(n + 1)
]

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

visited = [False] * (n + 1)

answer = 0
def dfs(node):
    global answer

    visited[node] = True

    for next_node in graph[node]:
        if not visited[next_node]:
            answer += 1
            dfs(next_node)


dfs(1)

print(answer)