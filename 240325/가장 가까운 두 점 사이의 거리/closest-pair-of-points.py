n = int(input())

points = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

answer = float('inf')
for i in range(n):
    for j in range(n):

        if i == j:
            continue

        x1, y1 = points[i]
        x2, y2 = points[j]

        answer = min(answer, (x2 - x1)**2 + (y2 - y1)**2)

print(answer)