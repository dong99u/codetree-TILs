N = int(input())

grid = []

max_val = 0
for _ in range(N):
    grid.append(list(map(int, input().split())))

for row in range(0, N - 2):
    for col in range(0, N - 2):
        cnt = 0
        for row_idx in range(0, 3):
            for col_idx in range(0, 3):
                value = grid[row + row_idx][col + col_idx]

                if value == 1:
                    cnt += 1
                
                if max_val < cnt:
                    max_val = cnt


print(max_val)