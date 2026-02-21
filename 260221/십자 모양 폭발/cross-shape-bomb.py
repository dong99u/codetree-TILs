n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())


# Please write your code here.
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

x, y = r - 1, c - 1
k = grid[x][y]

for dx, dy in zip(dxs, dys):

    for i in range(k):
        nx, ny = x + dx * i, y + dy * i

        if not in_range(nx, ny):
            break

        grid[nx][ny] = 0

answer_grid = [[0] * n for _ in range(n)]

for col_idx, col in enumerate(zip(*grid)):
    temp = []

    for num in col:
        if num != 0:
            temp.append(num)

    for i, num in enumerate(reversed(temp)):
        answer_grid[n - 1 - i][col_idx] = num

for row in answer_grid:
    print(*row)