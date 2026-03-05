n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
visited = [False] * n # 열에 대한 방문 여부


def backtrack(row, acc):
    '''
    row: 현재 row의 위치
    acc: 현재 노드까지의 누적값
    '''
    if row == n:
        return acc

    result = 0
    for col in range(n):
        if not visited[col]:
            visited[col] = True
            result = max(result, backtrack(row + 1, acc + grid[row][col]))
            visited[col] = False

    return result


answer = backtrack(0, 0)

print(answer)
