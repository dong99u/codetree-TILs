import sys
input = sys.stdin.readline

n, m = map(int, input().split())

a = set(map(int, input().split()))
b = set(map(int, input().split()))

c = a - b
d = b - a

print(len(c) + len(d))