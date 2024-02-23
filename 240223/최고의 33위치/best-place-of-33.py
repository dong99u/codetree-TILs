# 격자의 크기
N = int(input())

grid = [
    list(map(int, input().split()))
    for _ in range(N)
]

def in_range(row, col):
    return row <= N - 3 and col <= N - 3

# (row_s, col_s) ~ (row_e, col_e) 사이의 금의 개수를 계산하는 함수
def get_gold_in_grid(row_s, col_s, row_e, col_e):
    gold = 0

    for row in range(row_s, row_e + 1):
        for col in range(col_s, col_e + 1):
            gold += grid[row][col]

    return gold

max_gold = 0
for row in range(N):
    for col in range(N):
        if not in_range(row, col):
            continue

        gold = get_gold_in_grid(row, col, row + 2, col + 2)

        max_gold = max(max_gold, gold)

print(max_gold)