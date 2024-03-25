n, h, t = map(int, input().split())

ground = list(map(int, input().split()))

answer = 1000000000
for i in range(n - t + 1):
    sum_height = 0
    for j in range(i, i + t):

        sum_height += ground[j]

    if sum_height >= h * t:
        sum_move = 0
        for j in range(i, i + t):
            if ground[j] < h:
                sum_move += (h - ground[j]) * 2
        if sum_move != 0:
            answer = min(answer, sum_move)

print(answer)