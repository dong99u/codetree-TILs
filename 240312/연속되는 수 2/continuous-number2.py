n = int(input())

sequence = [
    int(input())
    for _ in range(n)
]

cnt = 1
max_cnt = 0



for i in range(1, n):
    
    if sequence[i] == sequence[i - 1]:
        cnt += 1

    else:
        cnt = 1

    max_cnt = max(max_cnt, cnt)

print(max_cnt)