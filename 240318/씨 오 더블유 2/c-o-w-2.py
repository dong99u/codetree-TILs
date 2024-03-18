n = int(input())
strs = input()

answer = 0
for i in range(n):
    if strs[i] == 'C':
        for j in range(i + 1, n):
            if strs[j] == 'O':
                for k in range(j + 1, n):
                    if strs[k] == 'W':

                        answer += 1
            
print(answer)