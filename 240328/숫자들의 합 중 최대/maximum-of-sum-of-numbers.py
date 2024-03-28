x, y = map(int, input().split())

answer = 0
for val in range(x, y + 1):
    vals = tuple(map(int, list(str(val))))

    answer = max(answer, sum(vals))

print(answer)