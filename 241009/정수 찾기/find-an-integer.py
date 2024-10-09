import sys

input = sys.stdin.readline

n = int(input().rstrip())

a = list(map(int, input().split()))

a = set(a)

m = int(input().rstrip())

b = list(map(int, input().split()))

for elem in b:
    if elem in a:
        print(1)
    else:
        print(0)