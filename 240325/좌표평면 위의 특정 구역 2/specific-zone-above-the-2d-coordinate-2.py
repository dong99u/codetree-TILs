n = int(input())

MAX = 40000

points = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

answer = float('inf')
for i in range(n):
    min_x, max_x = MAX, 1
    min_y, max_y = MAX, 1
    
    for j in range(n):

        if i == j:
            continue

        x, y = points[j]
        
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)

    answer = min(answer, (max_x - min_x) * (max_y - min_y))

print(answer)