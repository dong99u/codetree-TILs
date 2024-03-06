n = int(input())

sequence = []

answer = 0


def check_happy():
    global answer

    cnt = 1
    curr_num = sequence[0]

    arr = []
    for seq in sequence[1:]:
        if curr_num == seq:
            cnt += 1

        else:
            arr.append((curr_num, cnt))
            cnt = 1
        curr_num = seq

    arr.append((curr_num, cnt))

    if all([True if cnt % num == 0 else False for num, cnt in arr]):
        answer += 1

    # # 2의 개수가 2의 배수라면 행복
    # if all([arr[1] % 2 == 0, arr[2] % 3 == 0, arr[3] % 4 == 0]):
    #     answer += 1


def f(idx):

    # 종료 조건
    if idx == n:
        check_happy()
        return

    # 진행
    for num in range(1, 4 + 1):
        sequence.append(num)
        f(idx + 1)
        sequence.pop()


f(0)
print(answer)