def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def move_all(marbles):
    '''
    모든 구슬들의 위치를 이동시키는 함수
    :param marbles: x, y, d, w, i
    :return:
    '''
    nxt = [
        [[] for _ in range(n)]
        for _ in range(n)
    ]
    new_marbles = []
    for marble in marbles:
        x, y, d, w, num = marble
        nx, ny = x + dxs[d], y + dys[d]
        if not in_range(nx, ny): # 현재 위치가 벽이고, 다음 위치가 바깥으로 벗어나면 방향을 변경
            d = 3 - d
            nxt[x][y].append((x, y, d, w, num))
        else:
            nxt[nx][ny].append((nx, ny, d, w, num))

    for x in range(n):
        for y in range(n):
            if len(nxt[x][y]) > 1:
                w = sum([w for xi, yi, d, w, num in nxt[x][y]])
                _, _, d, _, num = max(nxt[x][y], key=lambda x:x[4])
                new_marbles.append((x, y, d, w, num))
            elif len(nxt[x][y]) == 1:
                _, _, d, w, num = nxt[x][y][0]
                new_marbles.append((x, y, d, w, num))

    return new_marbles

n, m, t = map(int, input().split())

marbles = []

mapper = {
    'D': 0,
    'L': 1,
    'R': 2,
    'U': 3,
}

dxs = [1, 0, 0, -1]
dys = [0, -1, 1, 0]

for i in range(m):
    ri, ci, di, wi = input().split()
    ri = int(ri) - 1
    ci = int(ci) - 1
    di = mapper[di]
    wi = int(wi)
    marbles.append((ri, ci, di, wi, i))

# Please write your code here.
for _ in range(t):
    marbles = move_all(marbles)

answer_weight = 0
answer_count = 0

for _, _, _, w, _ in marbles:
    if w > answer_weight:
        answer_weight = w
    answer_count += 1

print(answer_count, answer_weight)