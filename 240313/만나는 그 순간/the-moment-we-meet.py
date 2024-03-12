MAX_T = 1000000

n, m = tuple(map(int, input().split()))

A = [0] * (MAX_T + 1)
B = [0] * (MAX_T + 1)

time_a = 1
for _ in range(n):
    d, t = tuple(input().split())
    for _ in range(int(t)):
        A[time_a] = A[time_a - 1] + (1 if d == 'R' else -1)
        time_a += 1
    
time_b = 1
for _ in range(m):
    d, t = tuple(input().split())
    for _ in range(int(t)):
        B[time_b] = B[time_b - 1] + (1 if d == 'R' else -1)
        time_b += 1

answer = -1
for i in range(1, time_a):
    if A[i] == B[i]:
        answer = i
        break

print(answer)