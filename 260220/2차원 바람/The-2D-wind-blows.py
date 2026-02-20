from collections import deque

n, m, q = map(int, input().split())

# Create 2D array for building state
a = [list(map(int, input().split())) for _ in range(n)]

# Process wind queries
winds = [tuple(map(int, input().split())) for _ in range(q)]

# Please write your code here.

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def copy_to_queue(r1, c1, r2, c2):
    q = deque()
    for j in range(c1 - 1, c2):
        q.append(a[r1 - 1][j])

    for i in range(r1, r2):
        q.append(a[i][c2 - 1])

    for j in range(c2 - 2, c1 - 2, -1):
        q.append(a[r2 - 1][j])

    for i in range(r2 - 2, r1 - 1, -1):
        q.append(a[i][c1 - 1])

    return q


def copy_to_origin(r1, c1, r2, c2, q):
    for j in range(c1, c2 + 1):
        a[r1 - 1][j - 1] = q.popleft()

    for i in range(r1, r2):
        a[i][c2 - 1] = q.popleft()

    for j in range(c2 - 2, c1 - 2, -1):
        a[r2 - 1][j] = q.popleft()

    for i in range(r2 - 2, r1 - 1, -1):
        a[i][c1 - 1] = q.popleft()


def rotate(r1, c1, r2, c2):
    q = copy_to_queue(r1, c1, r2, c2)

    q.rotate(1)

    copy_to_origin(r1, c1, r2, c2, q)


for _ in range(q):
    for r1, c1, r2, c2 in winds:
        rotate(r1, c1, r2, c2)

        temp = [
            [0] * (c2 - c1 + 1)
            for _ in range(r2 - r1 + 1)
        ]

        for i in range(r1 - 1, r2):
            for j in range(c1 - 1, c2):
                sum_val = a[i][j]
                cnt = 1
                for di, dj in zip(dxs, dys):
                    nx, ny = i + di, j + dj

                    if not in_range(nx, ny):
                        continue

                    sum_val += a[nx][ny]
                    cnt += 1

                temp[i - r1 + 1][j - c1 + 1] = sum_val // cnt

        for i in range(r1 - 1, r2):
            for j in range(c1 - 1, c2):
                a[i][j] = temp[i - r1 + 1][j - c1 + 1]

for row in a:
    print(*row)