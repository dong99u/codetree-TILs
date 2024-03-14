import sys
input = sys.stdin.readline

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

n, t = tuple(map(int, input().split()))

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

# 명령들
instructions = input().strip()

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

x, y = n // 2, n // 2
answer = grid[x][y]
dir_num = 0

for instruction in instructions:
    if instruction == 'F':
        nx, ny = x + dx[dir_num], y + dy[dir_num]
        
        # 범위가 아니라면 무시
        if not in_range(nx, ny):
            continue

        x, y = nx, ny
        answer += grid[x][y]
        
    elif instruction == 'L':
        dir_num = (dir_num + 4 - 1) % 4
    else:
        dir_num = (dir_num + 1) % 4
    
print(answer)