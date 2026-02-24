n, m, r, c = map(int, input().split())
directions = list(input().split())

# Please write your code here.
top, bottom, left, right, front, back = 1, 6, 4, 3, 2, 5

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def move(d):
    global top, bottom, left, right, front, back

    if d == 'L':
        right, top, left, bottom = bottom, right, top, left
    elif d == 'R':
        left, top, right, bottom = bottom, left, top, right
    elif d == 'D':
        back, top, front, bottom = bottom, back, top, front
    elif d == 'U':
        front, top, back, bottom = bottom, front, top, back

grid = [
    [0] * n
    for _ in range(n)
]

cx, cy = r - 1, c - 1

for d in directions:
    grid[cx][cy] = bottom
    if d == 'L':
        nx, ny = cx, cy - 1
    elif d == 'R':
        nx, ny = cx, cy + 1
    elif d == 'D':
        nx, ny = cx + 1, cy
    elif d == 'U':
        nx, ny = cx - 1, cy
    
    if not in_range(nx, ny):
        continue
    
    cx, cy = nx, ny
    move(d)
    grid[cx][cy] = bottom

answer = 0

for i in range(n):
    for j in range(n):
        answer += grid[i][j]

print(answer)