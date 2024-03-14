n = int(input())

cows = [0]

cows.extend(list(map(int, input().split())))

answer = 0
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        for k in range(j + 1, n + 1):
            
            if cows[i] <= cows[j] <= cows[k]:
                answer += 1

print(answer)