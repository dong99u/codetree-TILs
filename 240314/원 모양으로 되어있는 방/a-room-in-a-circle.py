import sys
input = sys.stdin.readline

MAX_INT = sys.maxsize

n = int(input())

arr = [
    int(input())
    for _ in range(n)
]

min_dist = MAX_INT

for i in range(n):
    distance = 0

    for j in range(n):
        dist = (j + n - i) % n
        distance += dist * arr[j]

    min_dist = min(min_dist, distance)

print(min_dist)