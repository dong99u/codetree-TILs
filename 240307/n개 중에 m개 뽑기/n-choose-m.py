n, m = tuple(map(int, input().split()))

sequence = []


def print_answer():
    print(*sequence)


def choose(curr_num, cnt):

    # 종료 조건
    if curr_num == n + 1:
        if cnt == m:
            print_answer()
            return
        return

    # 진행 조건
    sequence.append(curr_num)
    choose(curr_num + 1, cnt + 1)
    sequence.pop()


    choose(curr_num + 1, cnt)

choose(1, 0)