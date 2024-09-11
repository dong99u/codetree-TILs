n = int(input())

jumps = list(map(int, input().split()))

answer = float('inf')
def back_track(current_index, count):
    global answer

    if current_index >= n - 1:
        answer = min(answer, count)
        return

    if jumps[current_index] == 0:
        return

    for jump in range(1, jumps[current_index] + 1):
        back_track(current_index + jump, count + 1)


back_track(0, 0)

if answer == float('inf'):
    print(-1)
else:
    print(answer)