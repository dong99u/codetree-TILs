import sys

input = sys.stdin.readline

n = int(input())

s1 = set(list(map(int, input().split())))

m = int(input())

s2 = list(map(int, input().split()))


for num in s2:
    if num in s1:
        print(1, end=' ')
    else:
        print(0, end=' ')