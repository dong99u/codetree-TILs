def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

# n x n 크기
n = int(input())

# 그리드 초기화
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

answer = 0

for curr_x in range(n):
    for curr_y in range(n):

        cnt = 0

        for dx, dy in zip(dxs, dys):
            nx = curr_x + dx
            ny = curr_y + dy

            if in_range(nx, ny) and grid[nx][ny] == 1:
                cnt += 1
        
        if cnt >= 3:
            answer += 1
            
print(answer)