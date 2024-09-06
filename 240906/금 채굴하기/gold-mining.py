n, m = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# (x, y)를 기준으로 마름모 모양 영역의 코인의 합을 구한다.
def get_cost(x, y, size):

    coin_count_sum = 0
    cost = (size * size + (size + 1) * (size + 1))

    if size == 0:
        return grid[x][y] - cost

    # 사각형 코인 더하기
    for i in range(x - size + 1, x + size):
        for j in range(y - size + 1, y + size):
            if not in_range(i, j):
                continue
            coin_count_sum += grid[i][j]

    # 각 동서남북 방향 코인 더하기
    if in_range(x, y - size):
        coin_count_sum += grid[x][y - size]
    if in_range(x, y + size):
        coin_count_sum += grid[x][y + size]
    if in_range(x - size, y):
        coin_count_sum += grid[x - size][y]
    if in_range(x + size, y):
        coin_count_sum += grid[x + size][y]

    coin_price_sum = coin_count_sum * m


    result_cost = coin_price_sum - cost

    return coin_count_sum if result_cost > 0 else 0



answer = 0
for x in range(n):
    for y in range(n):
        for k in range(n):
            cost = get_cost(x, y, k)
            if cost > 0:
                answer = max(answer, cost)

print(answer)