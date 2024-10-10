import sys
from sortedcontainers import SortedSet

input = sys.stdin.readline

n = int(input().rstrip())

s = SortedSet()

for _ in range(n):
    order = input().rstrip()

    if order.startswith('add'):
        s.add(int(order.split()[1]))

    elif order.startswith('remove'):
        s.discard(int(order.split()[1]))

    elif order.startswith('find'):
        print('true' if int(order.split()[1]) in s else 'false')

    elif order.startswith('lower_bound'):
        idx = s.bisect_left(int(order.split()[1]))

        if idx == len(s):
            print(None)
        else:
            print(s[idx])

    elif order.startswith('upper_bound'):
        idx = s.bisect_right(int(order.split()[1]))

        if idx == len(s):
            print(None)
        else:
            print(s[idx])


    elif order.startswith('largest'):
        print(s[-1] if s else None)

    elif order.startswith('smallest'):
        print(s[0] if s else None)