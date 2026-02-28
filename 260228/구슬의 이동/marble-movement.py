from collections import defaultdict

n, m, t, k = map(int, input().split())

r, c, d, v = [], [], [], []
for _ in range(m):
    ri, ci, di, vi = input().split()
    r.append(int(ri))
    c.append(int(ci))
    d.append(di)
    v.append(int(vi))

# Please write your code here.
# 상 좌 우 하
dxs = [-1, 0, 0, 1]
dys = [0, -1, 1, 0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bounce(pos, v, n, going_positive):
    """
    pos: 현재 위치 (0-indexed)
    v: 이동 거리
    n: 격자 크기 (0 ~ n-1)
    going_positive: True면 +방향, False면 -방향
    반환: (new_pos, new_going_positive)
    """
    period = 2 * (n - 1)

    # 방향에 따라 절대 좌표계로 변환
    # 양수 방향이면 pos 그대로, 음수 방향이면 "반사" 좌표 사용
    if going_positive:
        effective = (pos + v) % period
    else:
        effective = (pos - v) % period  # Python % 는 항상 양수

    if effective <= n - 1:
        return effective, True  # 양수 방향
    else:
        return period - effective, False  # 음수 방향

class Ball:
    def __init__(self, x=None, y=None, d=None, v=1, ball_num=1):
        self.x = x
        self.y = y
        self.d = d
        self.v = v
        self.ball_num = ball_num

    def move(self, n):
        if self.d in [0, 3]:  # 상하 이동
            going_positive = (self.d == 3)
            new_pos, new_going = bounce(self.x, self.v, n, going_positive)
            self.x = new_pos
            self.d = 3 if new_going else 0
        else:  # 좌우 이동
            going_positive = (self.d == 2)
            new_pos, new_going = bounce(self.y, self.v, n, going_positive)
            self.y = new_pos
            self.d = 2 if new_going else 1



mapper = {
    'U': 0,
    'L': 1,
    'R': 2,
    'D': 3,
}

grid = defaultdict(list)

for ball_num, (ri, ci, di, vi) in enumerate(zip(r, c, d, v)):
    ball = Ball(ri - 1, ci - 1, mapper[di], vi, ball_num + 1)
    grid[(ri - 1, ci - 1)].append(ball)

for _ in range(t):
    new_grid = defaultdict(list)
    for balls in grid.values():
        for ball in balls:
            ball.move(n)
            new_grid[(ball.x, ball.y)].append(ball)

    for coord, balls in new_grid.items():
        if len(balls) > k:
            balls.sort(key=lambda ball: (-ball.v, -ball.ball_num))
            new_grid[coord] = balls[:k]

    grid = new_grid

answer = 0
for balls in grid.values():
    answer += len(balls)

print(answer)
