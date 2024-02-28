A = list(input())

answer = float('inf')

for _ in range(len(A)):
    encoded_str = ''
    count = 1
    for i in range(1, len(A)):
        if A[i -1] == A[i]:
            count += 1
        else:
            encoded_str += str(A[i - 1]) + str(count)
    
    answer = min(answer, len(encoded_str))

print(answer)