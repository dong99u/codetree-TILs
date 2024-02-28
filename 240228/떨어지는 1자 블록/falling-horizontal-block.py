import sys

# 입력
n, m, k = tuple(map(int, sys.stdin.readline().split()))
k -= 1

grid = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]

# 다음 행의 모든 줄이 0이면 True
def all_blank(row) -> bool:
    global grid, m, k

    return all(value == 0 for value in grid[row][k:k + m])

def get_target_row():
    for row in range(n - 1):
        if not all_blank(row + 1):
            return row
    return n - 1

target_row = get_target_row()

for col in range(k, k + m):
    grid[target_row][col] = 1

for elem in grid:
    print(*elem)