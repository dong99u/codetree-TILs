def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def already_filled(x, y):
    return grid[x][y] != 0

n, m = map(int, input().split())

total_grid_cnt = n * m

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

grid = [[0] * m for _ in range(n)]

dir_num = 0 # 진행 방향

x, y = 0, 0
# 처음 시작 위치에 초깃값을 적음
grid[x][y] = 1

for cnt in range(2, total_grid_cnt + 1):
    nx, ny = x + dxs[dir_num], y + dys[dir_num]

    if not in_range(nx, ny) or already_filled(nx, ny):
        dir_num  = (dir_num + 1) % 4
    
    x, y = x + dxs[dir_num], y + dys[dir_num]
    grid[x][y] = cnt


for i in range(n):
    for j in range(m):
        print(grid[i][j], end=' ')
    print()