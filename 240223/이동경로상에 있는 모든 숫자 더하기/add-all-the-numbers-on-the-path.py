def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

N, T = map(int, input().split())


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 초기 방향은 북쪽
dir_num = 0

x, y = N // 2, N // 2

instructions = input()

grid = [
    list(map(int, input().split()))
    for _ in range(N)
]

answer = grid[x][y]

for instruction in instructions:
    if instruction == 'L':
        dir_num = (dir_num + 4 - 1) % 4
    if instruction == 'R':
        dir_num = (dir_num + 1) % 4
    if instruction == 'F':
        nx = x + dx[dir_num]
        ny = y + dy[dir_num]

        if not in_range(nx, ny):
            continue
        answer += grid[nx][ny]
        x, y = nx, ny

print(answer)