k, n = map(int, input().split())

result = []

def choose(curr_num):
    if curr_num >= n:
        print(*result)
        return

    for i in range(1, k + 1):
        result.append(i)
        choose(curr_num + 1)
        result.pop()


choose(0)