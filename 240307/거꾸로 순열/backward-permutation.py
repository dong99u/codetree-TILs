n = int(input())

visited = [False] * (n + 1)

answer = []

def choose(curr_num):
    
    # 종료 조건
    if curr_num == n + 1:
        print(*answer)
        return

    # 진행
    for i in range(n, 0, -1):

        # 이미 사용된 숫자라면
        if visited[i]:
            continue

        answer.append(i)
        visited[i] = True
        choose(curr_num + 1)

        answer.pop()
        visited[i] = False

choose(1)