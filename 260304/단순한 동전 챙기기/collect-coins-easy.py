n = int(input())
grid = [list(input()) for _ in range(n)]

# Please write your code here.
INF = float('inf')
pos = [None] * 10
S = None, None
E = None, None

for i in range(n):
    for j in range(n):
        if grid[i][j] == 'S':
            S = i, j
        elif grid[i][j] == 'E':
            E = i, j
        elif grid[i][j].isdigit():
            pos[int(grid[i][j])] = (i, j)


def get_dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x2 - x1) + abs(y2 - y1)

def backtrack(idx, acc, count, prev):
    if count == 3:
        return acc + get_dist(prev, E)
    result = INF
    for i in range(idx, 10):
        if pos[i] is None:
            continue
        if acc + get_dist(prev, pos[i]) < result:
            result = min(result, backtrack(i + 1, acc + get_dist(prev, pos[i]), count + 1, pos[i]))

    return result

answer = backtrack(1, 0, 0, S)
print(answer if answer != INF else -1)
