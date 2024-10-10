from sortedcontainers import SortedList

sl = SortedList()



T = int(input())
for _ in range(T):
    k = int(input())
    for _ in range(k):

        orders = input().split()

        order = orders[0]
        num = int(orders[1])

        if order == 'I':
            sl.add(num)
        elif order == 'D':
            if sl:
                if num == 1:
                    sl.pop()
                else:
                    sl.pop(0)

    if sl:
        print(sl[-1], sl[0])
    else:
        print('EMPTY')
    sl.clear()