n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

mapper = {
    1: [[-2, -1, 0, 1, 2], [0, 0, 0, 0, 0]],
    2: [[-1, 1, 0, 0, 0], [0, 0, -1, 1, 0]],
    3: [[-1, -1, 1, 1, 0], [-1, 1, 1, -1, 0]],
}

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# ✅ 핵심 1: 폭탄 위치를 미리 리스트로 모은다
#    → index로 관리하면 기저 조건이 명확해짐
bombs = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            bombs.append((i, j))

def backtrack(idx, bombed):
    # ✅ 핵심 2: 기저 조건 = 모든 폭탄을 다 결정했을 때
    if idx == len(bombs):
        return sum(bombed[i][j] for i in range(n) for j in range(n))

    x, y = bombs[idx]
    result = 0
    for bomb_type in range(1, 4):
        # ✅ 핵심 3: 깊은 복사로 되돌리기 대신 새 상태 생성
        new_bombed = [row[:] for row in bombed]
        for dx, dy in zip(*mapper[bomb_type]):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny):
                new_bombed[nx][ny] = 1
        result = max(result, backtrack(idx + 1, new_bombed))

    return result

bombed = [[0] * n for _ in range(n)]
print(backtrack(0, bombed))