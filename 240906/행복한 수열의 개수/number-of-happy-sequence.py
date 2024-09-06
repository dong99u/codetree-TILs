n, m = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

answer = 0

for row in range(n):
    prev = grid[row][0]
    continuous_row_count = 1

    if n <= 1:
        answer += 1
        continue

    for col in range(1, n):
        if prev == grid[row][col]:
            continuous_row_count += 1
        else:
            continuous_row_count = 1
        prev = grid[row][col]

        if continuous_row_count >= m:
            answer += 1
            break

for col in range(n):

    if n <= 1:
        answer += 1
        continue

    prev = grid[0][col]
    continuous_col_count = 1
    for row in range(1, n):
        if prev == grid[row][col]:
            continuous_col_count += 1
        else:
            continuous_col_count = 1
        prev = grid[row][col]

        if continuous_col_count >= m:
            answer += 1
            break

print(answer)