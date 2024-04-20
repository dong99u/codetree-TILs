x1, x2, x3, x4 = map(int, input().split())

answer = True

# 안 겹치는 경우
if (x1 < x3 and x2 < x3):
    answer = False
elif (x3 < x1 and x4 < x1):
    answer = False

if answer:
    print('intersecting')
else:
    print('nonintersecting')