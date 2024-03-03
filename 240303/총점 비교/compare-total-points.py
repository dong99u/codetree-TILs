n = int(input())

scores = [
    (name, int(score1), int(score2), int(score3)) for (name, score1, score2, score3) in (input().split() for _ in range(n))
]

scores.sort(key = lambda x: x[1] + x[2] + x[3])

for elem in scores:
    print(*elem)