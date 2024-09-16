import sys
input = sys.stdin.readline

n = int(input())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [False] * n
    for _ in range(n)
]

answer = 0
def back_track(row):
    global answer

    if row >= n:
        min_num = float('inf')

        for i in range(n):
            for j in range(n):
                if visited[i][j]:
                    min_num = min(min_num, grid[i][j])

        answer = max(answer, min_num)
        return

    for col in range(n):
        if is_valid(row, col):
            visited[row][col] = True
            back_track(row + 1)
            visited[row][col] = False

def is_valid(row, col):
    for i in range(row):
        if visited[i][col]:
            return False

    return True

back_track(0)

print(answer)