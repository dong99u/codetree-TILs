import sys
input = sys.stdin.readline

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 격자에서 원하는 숫자의 인덱스를 찾는 함수
def find_value(target):
    for i, row in enumerate(grid):
        if target in row:
            return (i, row.index(target))

def change(x, y):
    max_val, max_x, max_y = 0, -1, -1

    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy

        if not in_range(nx, ny):
            continue
        
        val = grid[nx][ny]
        if max_val < val:
            max_val, max_x, max_y = val, nx, ny

    grid[x][y], grid[max_x][max_y] = grid[max_x][max_y], grid[x][y]

# 입력
n, m = tuple(map(int, input().split()))

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 위의 방향에서부터 시계방향 순서
dxs = [-1, -1, 0, 1, 1, 1, 0, -1]
dys = [0, 1, 1, 1, 0, -1, -1, -1]

def turn_around():

    for num in range(1, n * n + 1):
        x, y = find_value(num)

        change(x, y)
        

                

# m번의 턴 수행
for _ in range(m):
    turn_around()

for row in grid:
    print(*row)