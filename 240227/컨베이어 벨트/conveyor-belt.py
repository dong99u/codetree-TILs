n, t = tuple(map(int, input().split()))

up = list(map(int, input().split()))
down = list(map(int, input().split()))


sum_up_down = up + down

for _ in range(t):
    temp = sum_up_down.pop(-1)
    sum_up_down.insert(0, temp)


print(*sum_up_down[:n])
print(*sum_up_down[n:])