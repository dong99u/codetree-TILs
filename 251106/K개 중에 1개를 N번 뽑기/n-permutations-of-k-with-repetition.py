K, N = map(int, input().split())

answer = []
# Please write your code here.
def dfs(cnt, selected):
    if cnt == N:
        answer.append(selected)
        return

    for num in range(1, K + 1):
        dfs(cnt + 1, selected + [num])

dfs(0, [])

for row in answer:
    for num in row:
        print(num, end=' ')
    print()