n, m, k = map(int, input().split())
numbers_2d = [list(map(int, input().split())) for _ in range(n)]


# Please write your code here.
def rotate():
    global numbers_2d

    temp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp[j][n - 1 - i] = numbers_2d[i][j]

    for j in range(n):
        temp_row = []
        for i in range(n):
            if temp[i][j] != 0:
                temp_row.append(temp[i][j])

        temp_row = [0] * (n - len(temp_row)) + temp_row

        for i in range(n):
            temp[i][j] = temp_row[i]

    numbers_2d = temp


def bomb():
    for j, col in enumerate(zip(*numbers_2d)):
        count = 1
        temp = []
        for i in range(1, n):
            if col[i] == 0:
                if col[i - 1] != 0 and count < m:
                    temp.extend([col[i - 1]] * count)
                count = 1
                continue

            if col[i - 1] == col[i]:
                count += 1
            else:
                if count < m:
                    temp.extend([col[i - 1]] * count)
                count = 1

        if count < m:
            temp.extend([col[n - 1]] * count)

        temp = [0] * (n - len(temp)) + temp

        for i in range(n):
            numbers_2d[i][j] = temp[i]


for _ in range(k + 1):
    bomb()
    rotate()

answer = 0
for i in range(n):
    for j in range(n):
        if numbers_2d[i][j] != 0:
            answer += 1

print(answer)






