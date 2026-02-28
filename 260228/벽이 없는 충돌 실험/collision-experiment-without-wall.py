from collections import defaultdict

t = int(input())

DIST = 1

class Marble:
    def __init__(self, x, y, d, weight, num):
        self.x = x
        self.y = y
        self.d = d
        self.weight = weight
        self.num = num

    def move(self):
        self.x += dxs[self.d] * DIST
        self.y += dys[self.d] * DIST

 # 우 상 좌 하
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

for _ in range(t):
    n = int(input())

    grid = defaultdict(list)

    mapper = {
        'R': 0,
        'U': 1,
        'L': 2,
        'D': 3,
    }

    for i in range(n):
        xi, yi, wi, di = input().split()
        xi, yi, wi = map(int, (xi, yi, wi))
        di = mapper[di]
        marble = Marble(xi * 2, yi * 2, di, wi, i + 1)
        grid[(xi, yi)].append(marble)

    answer = -1
    for time in range(4002):
        new_grid = defaultdict(list)
        for marbles in grid.values():
            for marble in marbles:
                marble.move()
                new_grid[(marble.x, marble.y)].append(marble)

        for pos, marbles in new_grid.items():
            if len(marbles) > 1:
                answer = time + 1
                final_marble = max(marbles, key=lambda m: (m.weight, m.num))
                new_grid[pos] = [final_marble]

        grid = new_grid


    print(answer)
