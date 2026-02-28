from collections import defaultdict
from itertools import combinations

t = int(input())
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]
mapper = {'R': 0, 'U': 1, 'L': 2, 'D': 3}

for _ in range(t):
    n = int(input())
    marbles = []

    for i in range(n):
        xi, yi, wi, di = input().split()
        xi, yi, wi = int(xi), int(yi), int(wi)
        di = mapper[di]
        marbles.append((xi*2, yi*2, di, wi, i+1))  # ← 2배 스케일

    collisions = defaultdict(list)

    for (xi, yi, di, wi, numi), (xj, yj, dj, wj, numj) in combinations(marbles, 2):
        dxi, dyi = dxs[di], dys[di]
        dxj, dyj = dxs[dj], dys[dj]

        ddx = dxi - dxj
        ddy = dyi - dyj

        if ddx == 0 and ddy == 0:
            continue

        if ddx == 0:
            if xi != xj:
                continue
            ct = (yj - yi) / ddy
        elif ddy == 0:
            if yi != yj:
                continue
            ct = (xj - xi) / ddx
        else:
            tx = (xj - xi) / ddx
            ty = (yj - yi) / ddy
            if tx != ty:
                continue
            ct = tx

        if ct <= 0 or ct != int(ct):
            continue

        collisions[int(ct)].append((numi, numj))

    alive = {m[4]: m for m in marbles}
    answer = -1

    for time in sorted(collisions.keys()):
        pos_group = defaultdict(list)

        for numi, numj in collisions[time]:
            if numi not in alive or numj not in alive:
                continue
            mi = alive[numi]
            cx = mi[0] + dxs[mi[2]] * time
            cy = mi[1] + dys[mi[2]] * time
            pos_group[(cx, cy)].extend([numi, numj])

        for pos, nums in pos_group.items():
            nums = list(set(nums))
            if len(nums) < 2:
                continue
            answer = time
            survivors = [alive[num] for num in nums if num in alive]
            best = max(survivors, key=lambda m: (m[3], m[4]))
            for num in nums:
                if num in alive:
                    del alive[num]
            alive[best[4]] = best

    print(answer)