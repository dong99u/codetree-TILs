n, k = tuple(map(int, input().split()))

answer = [0] * n

for _ in range(k):
    a, b = tuple(map(int, input().split()))
    a, b = a - 1, b - 1

    if a <= b:
        for i in range(a, b + 1):
            answer[i] += 1

    else:
        for i in range(a, b - 1, -1):
            answer[i] += 1

print(max(answer))