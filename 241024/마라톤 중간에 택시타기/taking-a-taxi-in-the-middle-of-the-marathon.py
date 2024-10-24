from collections import deque

n = int(input())

def get_taxi_distance(a: tuple, b: tuple):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

dist_l = deque()
dist_r = deque()

dist_l.appendleft(0)
dist_r.append(0)
for i in range(1, n):
    a = points[i - 1]
    b = points[i]
    distance = get_taxi_distance(a, b)

    dist_l.append(distance + dist_l[i - 1])

for i in range(n - 1, 0, -1):
    a = points[i]
    b = points[i - 1]

    distance = get_taxi_distance(a, b)

    dist_r.appendleft(distance + dist_r[0])

def get_jumped_index(index):
    sum = 0
    sum += dist_l[index - 1]
    sum += dist_r[index + 1]

    sum += get_taxi_distance(points[index - 1], points[index + 1])

    return sum

answer = 0

for i in range(1, n - 1):
    answer = min(answer, get_jumped_index(i))

print(answer)