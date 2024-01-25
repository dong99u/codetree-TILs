def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


# 격자의 크기 n x n
n = int(input())

# 격자
grid = [list(map(int, input().split())) for _ in range(n)]

# 터지는 좌표
x, y = map(int, input().split())

# 행렬이기 때문에 index로 바꾼다.
x, y = x - 1, y - 1

bomb_range = grid[x][y]

# 터지는 범위 내의 가로방향 격자 초기화
for col_idx in range(y - bomb_range + 1, y + bomb_range):
    if not in_range(x, col_idx):
        continue

    grid[x][col_idx] = 0

# 터지는 범위 내의 세로방향 격자 초기화
for row_idx in range(x - bomb_range + 1, x + bomb_range):
    if not in_range(row_idx, y):
        continue

    grid[row_idx][y] = 0

# 모두 0으로 초기화된 임시 격자 생성
temp_grid = [[0] * n for _ in range(n)]

# 떨어뜨리기
for col_idx in range(n):
    temp_grid_row_idx = n - 1
    for row_idx in range(n - 1, -1, -1):
        val = grid[row_idx][col_idx]
        if val == 0:
            continue
        temp_grid[temp_grid_row_idx][col_idx] = val
        temp_grid_row_idx -= 1


grid = temp_grid

for i in range(len(grid)):
    print(*grid[i])