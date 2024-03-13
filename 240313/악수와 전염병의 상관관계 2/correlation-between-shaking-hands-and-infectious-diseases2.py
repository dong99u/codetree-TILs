import sys
input = sys.stdin.readline

class Shake:
    def __init__(self, time, person1, person2):
        self.time, self.person1, self.person2 = time, person1, person2

n, k, p, t = tuple(map(int, input().split()))

MAX_TIME = 250

shakes = []

for _ in range(t):
    time, x, y = tuple(map(int, input().split()))
    shakes.append(Shake(time, x, y))

shakes.sort(key = lambda x: x.time)

shake_num = [0] * (n + 1)
infected = [False] * (n + 1)

infected[p] = True

for shake in shakes:
    x = shake.person1
    y = shake.person2

    if infected[x] == True:
        shake_num[x] += 1
    if infected[y] == True:
        shake_num[y] += 1

    if shake_num[x] <= k and infected[x]:
        infected[y] = True
    if shake_num[y]<= k and infected[y]:
        infected[x] = True

for i in range(1, n + 1):
    if infected[i]:
        print(1, end="")
    else:
        print(0, end="")