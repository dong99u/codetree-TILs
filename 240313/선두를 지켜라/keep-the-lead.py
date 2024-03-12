import sys
from enum import Enum


class Person(Enum):
    A = "A"
    B = "B"


input = sys.stdin.readline

MAX_TIME = 1000 * 1000
n, m = tuple(map(int, input().split()))

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

head = None
answer = 0
for i in range(1, curr_time_a):
    if A[i] < B[i]:
        if head != None and head != Person.B:
            answer += 1
        head = Person.B

    elif A[i] > B[i]:
        if head != None and head != Person.A:
            answer += 1
        head = Person.A


print(answer)