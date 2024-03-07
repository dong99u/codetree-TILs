n = int(input())

visited = [False] * (n + 1)

answer = []

def choose(curr_num):
    
    # 종료 조건
    if curr_num == n + 1:
        print(*answer)
        return

    # 진행 조건
    for i in range(1, n + 1):
        if visited[i]:
            continue

        visited[i] = True

        answer.append(i)
        choose(curr_num + 1)
        answer.pop()

        visited[i] = False

choose(1)