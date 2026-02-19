from collections import deque

n, t = map(int, input().split())

l = list(map(int, input().split()))
r = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.
q = deque([*l, *r, *d])

for _ in range(t):
    q.appendleft(q.pop())

for i in range(n):
    print(q[i], end=' ')
print()
for i in range(n, 2 * n):
    print(q[i], end=' ')
print()
for i in range(2 * n, 3 * n):
    print(q[i], end=' ')