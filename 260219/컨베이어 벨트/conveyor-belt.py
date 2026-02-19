from collections import deque

n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.
q = deque([*u, *d])
for _ in range(t):
    q.appendleft(q.pop())

for _ in range(3):
    print(q.popleft(), end=' ')
print()
for _ in range(3):
    print(q.popleft(), end=' ')