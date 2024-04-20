x1, x2, x3, x4 = map(int, input().split())

answer = False
if x3 <= x2 or x4 <= x1:
    answer = True

if answer:
    print('intersecting')
else:
    print('nonintersecting')