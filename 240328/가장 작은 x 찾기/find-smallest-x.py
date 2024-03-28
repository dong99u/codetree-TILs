n = int(input())

ranges = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

num = 1

while True:
    x = num
    cnt = 0

    for a, b in ranges:
        x *= 2
        if not a <= x <= b:
            break
        else:
            cnt += 1

    if cnt == n:
        break
    num += 1

print(num)