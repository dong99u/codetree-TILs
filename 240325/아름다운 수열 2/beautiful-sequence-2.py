n, m = map(int, input().split())

A = list(map(int, input().split()))
B = sorted(list(map(int, input().split())))

answer = 0
for i in range(n - m + 1):

    a_seq = sorted(A[i : i + m])
    if a_seq == B:
        answer += 1

print(answer)