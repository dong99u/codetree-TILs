n, m = map(int, input().split())

A = list(map(int, input().split()))
B = sorted(list(map(int, input().split())))

answer = 0
for i in range(n - 2):

    a_seq = sorted(A[i : i + 3])
    if a_seq == B:
        answer += 1

print(answer)