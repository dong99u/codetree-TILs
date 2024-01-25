# 수열 안에서 범위를 체크하는 함수
def in_range(idx):
    return idx + m <= n


# m개의 숫자가 모두 같은지 체크하는 함수
def same(lst):
    first_elem = lst[0]
    for elem in lst:
        if elem != first_elem:
            return False

    return True


# n: 격자의 크기 n x n
# m: 연속 해야하는 숫자의 개수
n, m = map(int, input().split())

happy_sequence_cnt = 0

grid = [list(map(int, input().split())) for _ in range(n)]

# 행 방향 수열 확인
for row_idx in range(len(grid)):
    for col_idx in range(len(grid[row_idx])):
        if not in_range(col_idx):
            break

        sequence = grid[row_idx][col_idx : col_idx + m]

        if same(sequence):
            happy_sequence_cnt += 1
            break


# 열 방향 수열 확인
for col_idx in range(len(grid[0])):
    for row_idx in range(len(grid)):
        if not in_range(row_idx):
            break

        sequence = [grid[row_idx + i][col_idx] for i in range(m)]

        if same(sequence):
            happy_sequence_cnt += 1
            break

print(happy_sequence_cnt)