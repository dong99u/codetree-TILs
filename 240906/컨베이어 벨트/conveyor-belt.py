n, t = map(int, input().split())

belt = []

for i in range(2):
    belt.extend(list(map(int, input().split())))

for _ in range(t):
    temp = belt[-1]
    for i in range(2 * n - 1, 0, -1):
        belt[i] = belt[i - 1]

    belt[0] = temp

print(*belt[:n])
print(*belt[n:])