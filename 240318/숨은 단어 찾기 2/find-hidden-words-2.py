def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

n, m = map(int, input().split())

grid = [input() for _ in range(n)]

dxs, dys = [0, 1, 1, 1, 0, -1, -1, -1], [1, 1, 0, -1, -1, -1, 0, 1]

answer = 0
for i in range(n):
    for j in range(m):
        
        for dx, dy in zip(dxs, dys):
            temp_strings = grid[i][j]

            cnt = 1
            curr_x = i
            curr_y = j   
            
            while True:
                nx = curr_x + dx
                ny = curr_y + dy

                if not in_range(nx, ny):
                    break

                temp_strings += grid[nx][ny]
                curr_x, curr_y = nx, ny
                cnt += 1

                if cnt == 3:
                    if temp_strings == 'LEE':
                        answer += 1
                    break

print(answer)