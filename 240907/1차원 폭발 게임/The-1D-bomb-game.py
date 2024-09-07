n, m = map(int, input().split())

bombs = []

for _ in range(n):
    bombs.append(int(input()))

def boom():
    left = 0
    right = 0

    def drop():
        nonlocal left, right
        global bombs

        temp = []

        for i in range(len(bombs)):
            if bombs[i] != 0:
                temp.append(bombs[i])

        bombs = temp

        left = right = 0

    count = 0
    while right < len(bombs):
        if bombs[left] == bombs[right]:
            right += 1
            count += 1
        else:
            if count >= m:
                for i in range(left, right):
                    bombs[i] = 0
                drop()
            left = right
            count = 0

    if count >= m:
        for i in range(left, right):
            bombs[i] = 0
        drop()

boom()

if len(bombs) == 0:
    print(0)
else:
    print(len(bombs))
    for elem in bombs:
        print(elem)