a, b, c = tuple(map(int, input().split()))

days = a - 11
hours = b - 11
minutes = c - 11

answer = 24 * days * 60 + 60 * hours + minutes

if answer < 0:
    print(-1)
else:
    print(answer)