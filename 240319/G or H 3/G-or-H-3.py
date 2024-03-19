n, k = map(int, input().split())

MAX_POS = 10000

G = 1
H = 2

arr = [0] * (MAX_POS + 1)

for _ in range(n):
    pos, alpha = input().split()
    pos = int(pos)

    arr[pos - 1] = alpha

answer = -1
for i in range(MAX_POS - k + 1):
    point = 0
    for j in range(i, i + k + 1):

        if arr[j] == 'G':
            point += 1
        elif arr[j] == 'H':
            point += 2

    answer = max(answer, point)

print(answer)