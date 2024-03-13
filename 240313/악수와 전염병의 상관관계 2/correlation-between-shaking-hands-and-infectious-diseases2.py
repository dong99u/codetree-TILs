import sys
input = sys.stdin.readline

n, k, p, t = tuple(map(int, input().split()))

MAX_TIME = 250

shakes = []

for _ in range(t):
    time, x, y = tuple(map(int, input().split()))
    shakes.append((time, x, y))

shakes.sort(key=lambda shake: shake[0])

infections = [None] * (n + 1)
infections[p] = k

for shake in shakes:
    time, x, y = shake

    # x와 y 개발자 둘다 감염되지 않았을 경우
    if infections[x] == None and infections[y] == None:
        continue

    # x개발자가 감염되고, y 개발자가 감염되지 않았을 경우
    elif infections[x] != None and infections[y] == None:
        if infections[x] > 0:
            infections[x] -= 1
            infections[y] = k

    # x 개발자가 감염되지 않았고, y 개발자가 감염됐을 경우
    elif infections[x] == None and infections[y] != None:
        if infections[y] > 0:
            infections[x] = k
            infections[y] -= 1

    # 둘다 감염됐을 경우
    else:
        infections[x] -= 1
        infections[y] -= 1


for i in range(1, n + 1):
    if infections[i] != None:
        print(1, end='')
    else:
        print(0, end='')