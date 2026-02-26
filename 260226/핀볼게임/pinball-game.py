n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

# / 모양 벽을 만났을 때 바뀌는 방향
mapper1 = {
    0: 1,
    1: 0,
    2: 3,
    3: 2
}

# \ 모양 벽을 만났을 때 바뀌는 방향
mapper2 = {
    0: 3,
    1: 2,
    2: 1,
    3: 0
}

dxs = [1, 0, -1, 0]
dys = [0, -1, 0, 1]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def change_direction(x, y, d):
    if grid[x][y] == 1:
        return mapper1[d]
    else:
        return mapper2[d]


def move(i, j, d):
    global answer
    time = 1

    while True:
        ni, nj = i + dxs[d], j + dys[d]
        time += 1

        if not in_range(ni, nj):
            break

        if grid[ni][nj] != 0:
            nd = change_direction(ni, nj, d)
            d = nd

        i, j = ni, nj

    return time


answer = 0

for j in range(n):
    i = 0
    d = 0
    answer = max(answer, move(i, j, d))

for i in range(n):
    j = n - 1
    d = 1
    answer = max(answer, move(i, j, d))

for j in range(n):
    i = n - 1
    d = 2
    answer = max(answer, move(i, j, d))

for i in range(n):
    j = 0
    d = 3
    answer = max(answer, move(i, j, d))

print(answer)