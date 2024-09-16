n = int(input())

visited = [False] * (n + 1)

result = []
def back_track(curr_num):
    if curr_num >= n:
        print(*result)
        return


    for i in range(1, n + 1):
        if visited[i]:
            continue

        result.append(i)
        visited[i] = True
        back_track(curr_num + 1)

        result.pop()
        visited[i] = False

back_track(0)