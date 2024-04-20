x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

answer = True


if x2 < a1:
    answer = False

elif a2 < x1:
    answer = False

elif y2 < b1:
    answer = False

elif b2 < y1:
    answer = False

if answer:
    print('overlapping')
else:
    print('nonoverlapping')