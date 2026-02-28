from collections import defaultdict

t = int(input())
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]
mapper = {'R': 0, 'U': 1, 'L': 2, 'D': 3}

for _ in range(t):
    n = int(input())
    grid = defaultdict(list)

    for i in range(n):
        xi, yi, wi, di = input().split()
        xi, yi, wi = int(xi), int(yi), int(wi)
        di = mapper[di]
        grid[(xi*2, yi*2)].append((xi*2, yi*2, di, wi, i+1))

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