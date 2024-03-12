n = int(input())

sequence = []
cnt = 1
max_cnt = 0

for _ in range(n):
    sequence.append(int(input()))

for i in range(1, n):
    
    if sequence[i] != sequence[i - 1]:
        max_cnt = max(max_cnt, cnt)
        cnt = 1

    else:
        cnt += 1

max_cnt = max(max_cnt, cnt)

print(max_cnt)