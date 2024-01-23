def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

n = int(input())

answer_cnt = 0

arr = []
for _ in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

for row_idx in range(n):
    for col_idx in range(n):
        
        cnt = 0

        for dx, dy in zip(dxs, dys):
            nx = row_idx + dx
            ny = col_idx + dy

            if not in_range(nx, ny):
                continue
            
            if arr[nx][ny] == 1:
                cnt += 1

        if cnt >= 3:
            answer_cnt += 1   

print(answer_cnt)