k, n = tuple(map(int, input().split()))

answer = []


def choose(idx):
    if idx == n + 1:
        print(*answer)
        return

    for num in range(1, k + 1):
        answer.append(num)
        choose(idx + 1)
        answer.pop()


choose(1)