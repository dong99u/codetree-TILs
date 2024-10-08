import sys

input = sys.stdin.readline

n = int(input().rstrip())

s = set()

for _ in range(n):
    order, num = input().split()

    if order == 'add':
        s.add(num)
    elif order == 'remove':
        s.remove(num)
    elif order == 'find':
        if num in s:
            print('true')
        else:
            print('false')