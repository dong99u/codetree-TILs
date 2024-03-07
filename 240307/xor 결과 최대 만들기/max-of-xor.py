from functools import reduce
import operator


def xor_operands(*operands):
    global answer
    result = reduce(operator.xor, operands)
    answer = max(answer, result)
    return


n, m = tuple(map(int, input().split()))

nums = list(map(int, input().split()))

selected = []

answer = 0


# curr_num 번째의 숫자 선택
def choose(curr_num, cnt):

    # 종료 조건

    if curr_num == n + 1:
        if cnt == m:
            arr = []
            for idx, num in enumerate(selected):
                if num == 1:
                    arr.append(nums[idx])
            xor_operands(*arr)
            return
        return

    selected.append(1)
    choose(curr_num + 1, cnt + 1)
    selected.pop()

    selected.append(0)
    choose(curr_num + 1, cnt)
    selected.pop()


choose(1, 0)

print(answer)