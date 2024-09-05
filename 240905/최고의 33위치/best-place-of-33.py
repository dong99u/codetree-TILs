n = int(input())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]


# 3x3 격자의 코인의 값을 가져오는 함수
def get_num_of_gold(row_s, col_s):
    result = 0
    for row in range(row_s, row_s + 2 + 1):
        for col in range(col_s, col_s + 2 + 1):

            if row >= n or col >= n:
                return

            result += grid[row][col]

    return result


answer = 0

for row in range(n):
    for col in range(n):

        result = get_num_of_gold(row, col)
        if result:
            answer = max(answer, result)

print(answer)