dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

# 현재 위치가 편안한 상태인지 확인하는 함수
# 편안하면 return True
def is_comfortable(x, y):
    count = 0
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy

        if in_range(nx, ny) and grid[nx][ny] == 1:
            count += 1

    if count == 3: return True
    else: return False

# N: N x N 격자
# M: 색칠 횟수
N, M = map(int, input().split())

# 격자 초기화
grid = [
    [0] * N
    for _ in range(N)
]

for _ in range(M):
    # 색칠할 좌표
    r, c = map(int, input().split())
    
    # 행과 열에서 리스트 인덱스로 변환
    r, c = r - 1, c - 1 

    grid[r][c] = 1

    if is_comfortable(r, c):
        print(1)
    else:
        print(0)