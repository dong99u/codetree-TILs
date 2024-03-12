n, m, k = tuple(map(int, input().split()))

students = [0] * (n + 1)

answer = -1
for _ in range(m):

    student_num = int(input())

    students[student_num] += 1

    if students[student_num] >= k:
        answer = student_num
        break

print(answer)