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
        xi, yi, wi = int(xi), int(yi), int(wi)
        di = mapper[di]
        grid[(xi * 2, yi * 2)].append((xi * 2, yi * 2, di, wi, i + 1))

    answer = -1
    for time in range(1, 4003):
        new_grid = defaultdict(list)
        total = sum(len(v) for v in grid.values())
        if total <= 1:
            break

        for marbles in grid.values():
            for x, y, d, w, num in marbles:
                nx, ny = x + dxs[d], y + dys[d]
                new_grid[(nx, ny)].append((nx, ny, d, w, num))

        for pos, marbles in new_grid.items():
            if len(marbles) > 1:
                answer = time
                best = max(marbles, key=lambda m: (m[3], m[4]))
                new_grid[pos] = [best]

        grid = new_grid

    print(answer)
