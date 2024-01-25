# n: 격자의 크기 n x n
# m: 떨어지는 블록의 크기 1 x m
# k: 블록이 떨어질 위치 정보 (k 번째 열부터 k + m - 1 번째 열까지 공간 차지)
n, m, k = map(int, input().split())

# 격자 초기화
grid = [list(map(int, input().split())) for _ in range(n)]

# 행렬의 정보이므로 index 값으로 바꿈
k = k - 1

# 해당 row에 col_s 부터 col_e 까지 열에 전부 블럭이 없는지 확인
# 모두 0이면 True
def all_blank(row: int, col_s: int, col_e: int) -> bool:
    return all([not grid[row][col] for col in range(col_s, col_e + 1)])

def get_target_row() -> int:
    for row in range(n - 1):
        if not all_blank(row + 1, k, k + m - 1):
            return row

    return n - 1
        
target_now = get_target_row()

# 블럭 표시
for col in range(k, k + m):
    grid[target_now][col] = 1

for row in grid:
    print(*row)