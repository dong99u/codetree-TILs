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
        marbles.append((xi, yi, di, wi, i+1))

    # 충돌 시간별로 (i번, j번) 쌍 수집
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
            if ddy == 0:
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

        # 양의 정수 시간이어야 유효
        if ct <= 0 or ct != int(ct):
            continue

        collisions[int(ct)].append((numi, numj))

    # 구슬 정보 딕셔너리 (num -> (weight, num))
    alive = {m[4]: m for m in marbles}  # num -> marble tuple

    answer = -1

    for time in sorted(collisions.keys()):
        # 같은 시간에 발생하는 충돌들을 위치별로 묶기
        pos_group = defaultdict(list)

        for numi, numj in collisions[time]:
            if numi not in alive or numj not in alive:
                continue
            mi = alive[numi]
            mj = alive[numj]
            # 충돌 위치 계산
            cx = mi[0] + dxs[mi[2]] * time
            cy = mi[1] + dys[mi[2]] * time
            pos_group[(cx, cy)].extend([numi, numj])

        for pos, nums in pos_group.items():
            nums = list(set(nums))  # 중복 제거
            if len(nums) < 2:
                continue
            answer = time
            # 무게 최대, 같으면 번호 최대인 구슬 생존
            survivors = [alive[num] for num in nums if num in alive]
            best = max(survivors, key=lambda m: (m[3], m[4]))
            for num in nums:
                if num in alive:
                    del alive[num]
            alive[best[4]] = best

    print(answer)