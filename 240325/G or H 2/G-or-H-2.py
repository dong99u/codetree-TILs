n = int(input())

MAX_POS = 100

arr = [0] * (MAX_POS + 1)

for _ in range(n):
    x, alpha = input().split()
    x = int(x)

    arr[x] = alpha

answer = 0
for i in range(MAX_POS + 1):
    for j in range(i + 1, MAX_POS + 1):
        
        if arr[i] == 0 or arr[j] == 0:
            continue

        g_cnt = 0
        h_cnt = 0

        for k in range(i, j + 1):
            if arr[k] == 'G':
                g_cnt += 1
            elif arr[k] == 'H':
                h_cnt += 1

        if g_cnt == h_cnt:
            answer = max(answer, j - i)
            
            

print(answer)