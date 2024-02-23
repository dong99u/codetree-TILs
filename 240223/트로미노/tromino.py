# 각 모양별로 틀 안의 숫자의 합을 구하는 함수
def get_sum_each_shape(row_s, col_s, row_e, col_e):
    """
    ㅁ
    ㅁㅁ
    """
    sum_a = sum((grid[row_s][col_s], grid[row_e][col_s], grid[row_e][col_e]))

    """
    ㅁㅁ
    ㅁ
    """
    sum_b = sum((grid[row_s][col_s], grid[row_s][col_e], grid[row_e][col_s]))

    """
    ㅁㅁ
     ㅁ
    """
    sum_c = sum((grid[row_s][col_s], grid[row_s][col_e], grid[row_e][col_e]))

    """
     ㅁ
    ㅁㅁ
    """
    sum_d = sum((grid[row_s][col_e], grid[row_e][col_s], grid[row_e][col_e]))

    return max(sum_a, sum_b, sum_c, sum_d)


def get_sum_row(row, col_s, col_e):
    return sum(grid[row][col_s : col_e + 1])


def get_sum_col(row_s, row_e, col):
    return sum([grid[row][col] for row in range(row_s, row_e + 1)])


n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

answer = 0

for row in range(n):
    for col in range(m):
        # 1 x 3 범위 안
        if col + 2 < m:
            row_sum = get_sum_row(row, col, col + 2)
            answer = max(answer, row_sum)
        # 3 x 1 범위 안
        if row + 2 < n:
            col_sum = get_sum_col(row, row + 2, col)
            answer = max(answer, col_sum)


for row in range(n):
    for col in range(m):

        # 2 x 2사각형 범위 안
        if row + 1 <= 2 and col + 1 <= 2:
            # 그 2x2 사각형 안에서 최대 크기를 구함
            max_sum_in_square = get_sum_each_shape(row, col, row + 1, col + 1)
            answer = max(answer, max_sum_in_square)

print(answer)