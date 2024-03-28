n = int(input())

sequence = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

cups = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]
answer = 0
for cup in cups:
    points = 0
    for a, b, c in sequence:

        cup[a - 1], cup[b - 1] = cup[b - 1], cup[a - 1]
        points += cup[c - 1]

    answer = max(answer, points)


print(answer)