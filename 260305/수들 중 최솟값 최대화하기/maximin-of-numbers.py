n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
visited = [False] * n
INF = float('inf')

def backtrack(row, min_val):
    '''
    row: 현재 노드가 위치한 row의 인덱스
    acc: 이전까지 선택한 값들의 합
    '''

    if row == n:
        return min_val

    result = 0
    for col in range(n):
        if visited[col]:
            continue
        visited[col] = True
        result = max(result, backtrack(row + 1, min(min_val, grid[row][col])))
        visited[col] = False

    return result

answer = backtrack(0, INF)

print(answer)