n, m = tuple(map(int, input().split()))

sequence = []


def print_answer():
    for idx, seq in enumerate(sequence):
        if seq == 1:
            print(idx + 1, end=" ")
    print()


def choose(curr_num, cnt):

    # 종료 조건
    if curr_num == n + 1:
        if cnt == m:
            print_answer()
            return
        return

    # 진행 조건
    sequence.append(1)
    choose(curr_num + 1, cnt + 1)
    sequence.pop()

    sequence.append(0)
    choose(curr_num + 1, cnt)
    sequence.pop()


choose(1, 0)