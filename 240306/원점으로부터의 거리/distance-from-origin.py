N = int(input())

points = [
    (int(x), int(y), idx + 1) for idx, (x, y) in enumerate(input().split() for _ in range(N))
]


points.sort(key=lambda x: abs(x[0]) + abs(x[1]))

for point in points:
    print(point[-1])