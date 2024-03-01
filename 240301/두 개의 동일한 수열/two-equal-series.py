n = int(input())

A = set(list(map(int, input().split())))
B = set(list(map(int, input().split())))


if A == B:
    print('Yes')
else:
    print('No')