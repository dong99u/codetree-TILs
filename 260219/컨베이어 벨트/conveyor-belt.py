n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.
for _ in range(t):
    u_temp = u[-1]
    for i in range(n - 1, 0, -1):
        u[i] = u[i - 1]
    
    d_temp = d[-1]
    for i in range(n - 1, 0, -1):
        d[i] = d[i - 1]

    u[0] = d_temp
    d[0] = u_temp

print(*u)
print(*d)