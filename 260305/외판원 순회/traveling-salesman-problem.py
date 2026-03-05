n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
INF = float('inf')
visited = [False] * n
visited[0] = True

def backtrack(curr, acc, count):
    if count == n:
        if A[curr][0] == 0:
            return INF
        return acc + A[curr][0]

    result = INF
    for nxt in range(1, n):
        if not visited[nxt]:
            if A[curr][nxt] == 0:
                continue
            next_dist = acc + A[curr][nxt]
            if next_dist > result:
                continue
            visited[nxt] = True
            result = min(result, backtrack(nxt, next_dist, count + 1))
            visited[nxt] = False

    return result

answer = backtrack(0, 0, 1)

print(answer)