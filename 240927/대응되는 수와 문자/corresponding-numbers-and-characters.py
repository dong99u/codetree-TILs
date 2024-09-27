import sys
input = sys.stdin.readline

n, m = map(int, input().split())

a = dict()
b = dict()

for i in range(1, n + 1):
    alphabet = input().rstrip()

    a[i] = alphabet
    b[alphabet] = i

for _ in range(m):
    find_input = input().rstrip()

    if find_input.isdigit():
        print(a[int(find_input)])

    else:
        print(b[find_input])