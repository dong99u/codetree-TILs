a, b, c = tuple(map(int, input().split()))

days = a - 11
hours = b - 11
minutes = c - 11

answer = 24 * days * 60 + 60 * hours + minutes

print(answer)