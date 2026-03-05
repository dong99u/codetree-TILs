n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
INF = float('inf')
selected = []

def get_max_dist():
    result = -1
    for i in range(m):
        for j in range(i + 1, m):
            dist = get_dist(selected[i], selected[j])
            result = max(result, dist)

    return result


def get_dist(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

def backtrack(idx, count):
    if count == m:
        max_dist = get_max_dist()
        return max_dist

    result = INF
    for i in range(idx, n):
        selected.append(points[i])
        result = min(result, backtrack(i + 1, count + 1))
        selected.pop()

    return result

answer = int(backtrack(0, 0))

print(answer)