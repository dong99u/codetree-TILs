n = int(input())

sequence = []
cnt = 0

for _ in range(n):
    sequence.append(int(input()))

for i in range(n):
    if i == 0 or sequence[i] != sequence[i - 1]:
        cnt += 1

print(cnt)