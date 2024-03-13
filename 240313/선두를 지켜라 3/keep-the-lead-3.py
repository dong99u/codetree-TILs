from enum import Enum


class Person(Enum):
    A = "A"
    B = "B"
    AB = "AB"


n, m = tuple(map(int, input().split()))

MAX_TIME = 1000 * 1000

A = [0] * (MAX_TIME + 1)
B = [0] * (MAX_TIME + 1)

curr_time_a = 1
for _ in range(n):

    v, t = tuple(map(int, input().split()))

    for _ in range(t):
        A[curr_time_a] = A[curr_time_a - 1] + v
        curr_time_a += 1

curr_time_b = 1
for _ in range(m):

    v, t = tuple(map(int, input().split()))

    for _ in range(t):
        B[curr_time_b] = B[curr_time_b - 1] + v
        curr_time_b += 1

answer = 0
head = None

for time in range(1, curr_time_a):
    if A[time] < B[time]:
        if head != Person.B:
            answer += 1
        head = Person.B

    elif A[time] > B[time]:
        if head != Person.A:
            answer += 1
        head = Person.A

    else:
        if head != Person.AB:
            answer += 1
        head = Person.AB

print(answer)