from collections import deque

A = input()

# Please write your code here.
def check():
    pass

q = deque(A)

answer = 1e9

for _ in range(len(A)):
    cnt = 1
    result = []
    for i in range(1, len(A)):
        if q[i - 1] == q[i]:
            cnt += 1
        else:
            result.append(q[i - 1])
            result.append(cnt)
            cnt = 1
    result.append(q[len(A) - 1])
    result.append(cnt)

    answer = min(answer, len(''.join(map(str, result))))

    q.rotate(1)

print(answer)