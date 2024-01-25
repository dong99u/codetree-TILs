n, t = list(map(int, input().split()))

belt = []

total_elements_cnt = n * 2
for _ in range(2):
    row = list(map(int, input().split()))
    belt.extend(row)

for _ in range(t):
    temp = belt[-1]

    for idx in range(total_elements_cnt - 2, -1, -1):
        belt[idx + 1] = belt[idx]

    belt[0] = temp

for idx in range(0, total_elements_cnt, n):
    print(*belt[idx : idx + n])