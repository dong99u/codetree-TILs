import sys

n = int(input())
sx, sy = map(int, input().split())
grid = [input() for _ in range(n)]

cx, cy = sx - 1, sy - 1

# 방향: 우(0), 하(1), 좌(2), 상(3)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
d = 0  # 처음 우측

# visited[x][y][dir] : 같은 위치+같은 방향이 반복되면 무한루프
visited = [[[False] * 4 for _ in range(n)] for _ in range(n)]
time = 0


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def is_wall(x, y):
    """격자 안에 있으면서 벽인 경우만 True (격자 밖은 벽이 아님)"""
    return in_range(x, y) and grid[x][y] == '#'


while in_range(cx, cy):
    # 무한루프 탐지: 같은 위치에서 같은 방향이면 영원히 반복
    if visited[cx][cy][d]:
        print(-1)
        sys.exit()
    visited[cx][cy][d] = True

    nx, ny = cx + dx[d], cy + dy[d]

    # Step 1: 앞에 벽 → 반시계 90도 회전만 (이동 없음)
    if is_wall(nx, ny):
        d = (d - 1) % 4

    # Step 2 - Case 1: 앞이 격자 밖 → 탈출
    elif not in_range(nx, ny):
        time += 1
        break

    # Step 2 - Case 2 & 3: 앞이 이동 가능한 빈 칸
    else:
        rd = (d + 1) % 4  # 오른쪽 방향
        rx, ry = nx + dx[rd], ny + dy[rd]  # 이동 후 오른쪽 좌표

        # Case 2: 오른쪽에 벽 있음 → 1칸 전진
        if is_wall(rx, ry):
            cx, cy = nx, ny
            time += 1

        # Case 3: 오른쪽에 벽 없음 → 2칸 이동 + 시계방향 회전
        else:
            cx, cy = rx, ry
            d = rd
            time += 2

print(time)