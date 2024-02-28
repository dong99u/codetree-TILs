import sys

# 입력
n, m, k = tuple(map(int, sys.stdin.readline().split()))
k -= 1

grid = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]

# 다음 행의 모든 줄이 0이면 True
# row: 다음 행
def can_land(row) -> bool:
    global grid, m, k

    return all(value == 0 for value in grid[row][k:k + m])

def land(row):
    global grid, m ,k

    for col in range(k, k + m):
        grid[row][col] = 1

for row in range(n):

    if not can_land(row):
        land(row - 1)
        break
    
for row in grid:
    print(*row)