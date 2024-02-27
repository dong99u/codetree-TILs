n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

def positive_rect(x1, y1, x2, y2):
    return all([
        grid[i][j] > 0
        for i in range(x1, x2 + 1)
        for j in range(y1, y2 + 1)
    ])

answer = -1

for i in range(n):
    for j in range(m):
        for k in range(i, n):
            for l in range(j, m):
                if positive_rect(i, j, k, l):
                    answer = max(answer, (k - i + 1) * (l - j + 1))

print(answer)