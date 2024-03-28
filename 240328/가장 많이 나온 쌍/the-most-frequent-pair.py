n, m = map(int, input().split())

arr = [
    tuple(map(int, input().split()))
    for _ in range(m)
]

answer = 0

def count_num(first, second):
    cnt = 0

    for a, b in arr:
        if (first, second) in [(a, b), (b, a)]:
            cnt += 1

    return cnt

for i in range(1, n + 1):
    for j in range(i + 1, n + 1):

        cnt = count_num(i, j)

        answer = max(answer, cnt)

print(answer)