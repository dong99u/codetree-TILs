# 각 모양별로 틀 안의 숫자의 합을 구하는 함수
def get_sum_each_shape(row_s, col_s, row_e, col_e):
    '''
    ㅁ
    ㅁㅁ
    '''
    sum_a = sum((
        grid[row_s][col_s],
        grid[row_e][col_s],
        grid[row_e][col_e]
    ))

    '''
    ㅁㅁ
    ㅁ
    '''
    sum_b = sum((
        grid[row_s][col_s],
        grid[row_s][col_e],
        grid[row_e][col_s]
    ))

    '''
    ㅁㅁ
     ㅁ
    '''
    sum_c = sum((
        grid[row_s][col_s],
        grid[row_s][col_e],
        grid[row_e][col_e]
    ))

    '''
     ㅁ
    ㅁㅁ
    '''
    sum_d = sum((
        grid[row_s][col_e],
        grid[row_e][col_s],
        grid[row_e][col_e]
    ))

    return max(sum_a, sum_b, sum_c, sum_d)

n, m = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

max_sum = 0

'''
ㅁㅁㅁ
'''
for row in grid:
    sum_val = sum(row)
    max_sum = max(max_sum, sum_val)

'''
ㅁ
ㅁ
ㅁ
'''
for col in list(zip(*grid)):
    sum_val = sum(col)
    max_sum = max(max_sum, sum_val)


for row in range(n):
    for col in range(m):
        # 범위 안에 있으면
        if row + 1 <= 2 and col + 1 <= 2:
            # 그 2x2 사각형 안에서 최대 크기를 구함
            max_sum_in_square = get_sum_each_shape(row, col, row + 1, col + 1)
            max_sum = max(max_sum, max_sum_in_square)

print(max_sum)