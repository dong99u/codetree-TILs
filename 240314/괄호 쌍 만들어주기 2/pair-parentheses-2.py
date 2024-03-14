a = input()

answer = 0
for i in range(1, len(a) - 2):
    if a[i - 1] == a[i] == '(':

        for j in range(i + 1, len(a) - 1):
            if a[j] == a[j + 1] == ')':
                answer += 1

print(answer)