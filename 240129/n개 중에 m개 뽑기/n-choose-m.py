n, m = map(int, input().split())
answer = []

def print_answer():
    for i in range(n):
        if answer[i] == 1:
            print(i + 1, end=' ')
    print()


    # for elem in answer:
    #     print(elem, end=' ')
    # print()

def choose(curr_num, cnt):
    if curr_num == n + 1:
        if cnt == m:
            print_answer()
        return

    answer.append(1)
    choose(curr_num + 1, cnt + 1)
    answer.pop()
    
    answer.append(0)
    choose(curr_num + 1, cnt)
    answer.pop()

    

choose(1, 0)