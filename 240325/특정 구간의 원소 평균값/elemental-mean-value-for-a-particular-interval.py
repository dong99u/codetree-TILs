n = int(input())

arr = list(map(int, input().split()))

answer = 0
# i: 구간의 시작점
# j: 구간의 끝점
for i in range(n):
    for j in range(i, n):
        cnt = j - i + 1
        average = sum(arr[i : j + 1]) / cnt


        for k in range(i, j + 1):
            if arr[k] == average:
                answer += 1
                break

print(answer)