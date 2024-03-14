sequence = input()

end = len(sequence)
answer = 0

for start in range(end):
    if sequence[start] == '(':
    
        for i in range(start + 1, end):
            if sequence[i] == ')':
                answer += 1

print(answer)