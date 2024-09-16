n, m = map(int, input().split())

result = []

def print_number():
    for idx, num in enumerate(result):
        if num == 1:
            print(idx + 1, end=" ")
    print()

def back_track(curr_num, cnt):
    if curr_num >= n + 1:
        return

    if cnt >= m:
        print_number()
        return

    result.append(1)
    back_track(curr_num + 1, cnt + 1)
    result.pop()

    result.append(0)
    back_track(curr_num + 1, cnt)
    result.pop()




back_track(0, 0)