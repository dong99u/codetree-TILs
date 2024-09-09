n = int(input())

result = []

answer = 0
def is_beautiful():
    global answer

    prev = None
    count = 0
    beautiful = True

    for number in result:
        if number != prev:
            if prev is not None and count != prev:
                beautiful = False
                break
            prev = number
            count = 1
        else:
            count += 1

    if beautiful and count != prev:
        beautiful = False

    if beautiful:
        answer += 1

def back_tracking(curr_num: int):
    if curr_num >= n:
        is_beautiful()
        return

    for i in range(1, 4 + 1):
        result.append(i)
        back_tracking(curr_num + 1)
        result.pop()


back_tracking(0)
print(answer)