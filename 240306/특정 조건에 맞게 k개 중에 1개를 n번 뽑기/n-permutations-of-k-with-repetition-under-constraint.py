k, n = tuple(map(int, input().split()))

answer = []

def choose(curr_num):
    # 종료 조건
    if curr_num == n + 1:
        print(*answer)
        return

    # 진행 조건
    for num in range(1, k + 1):
        if len(answer) > 2 and answer[-1] == num and answer[-2] == num:
            continue

        answer.append(num)
        choose(curr_num + 1)
        answer.pop()
        

choose(1)