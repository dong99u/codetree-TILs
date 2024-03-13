import sys

input = sys.stdin.readline

n, m = tuple(map(int, input().split()))

MAX_TIME = 1000000

A = [0] * MAX_TIME
B = [0] * MAX_TIME

curr_time_a = 1
for _ in range(n):
    t, d = input().split()

    for _ in range(int(t)):

        A[curr_time_a] = A[curr_time_a - 1] + (1 if d == "R" else -1)
        curr_time_a += 1

curr_time_b = 1
for _ in range(m):
    t, d = input().split()

    for _ in range(int(t)):

        B[curr_time_b] = B[curr_time_b - 1] + (1 if d == "R" else -1)
        curr_time_b += 1

if curr_time_a < curr_time_b:
    for i in range(curr_time_a, curr_time_b + 1):
        A[i] = A[i - 1]
else:
    for i in range(curr_time_b, curr_time_a + 1):
        B[i] = B[i - 1]

answer = 0
exit_time = max(curr_time_a, curr_time_b)
for time in range(1, exit_time + 1):

    if A[time] == B[time] and (A[time - 1] != B[time - 1]):
        answer += 1

print(answer)