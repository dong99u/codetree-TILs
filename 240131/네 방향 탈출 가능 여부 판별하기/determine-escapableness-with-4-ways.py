from collections import deque

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m
n, m = map(int, input().split())

# 지도 입력
a = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [0 for _ in range(m)]
    for _ in range(n)
]

def bfs():
    # queue를 가지고 너비 우선 탐색
    while q:
        r, c = q.popleft() # 현재 위치가 r행 c열을 탐색 중이다.

        for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nr, nc = r + dr, c + dc # r, c와 인접한 칸인 (nr, nc) 찾기

            # 격자를 벗어나지 않는 지        / 뱀이 없는지 / 방문한 적이 없는지
            if in_range(nr, nc) and a[nr][nc] == 1 and not visited[nr][nc]:
                visited[nr][nc] = 1
                q.append((nr, nc))
            


q = deque() # 새로운 queue를 생성
visited[0][0] = 1 # (0, 0)은 탐색 성공
q.append((0, 0))  # (0, 0)은 탐색 가능하다고 queue에 추가하기

bfs() # 탐색 수행

print(visited[n - 1][m - 1])