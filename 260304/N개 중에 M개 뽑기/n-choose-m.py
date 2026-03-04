N, M = map(int, input().split())

# Please write your code here.
selected = []

def backtrack(start, depth):
    if depth == M:
        print(*selected)
        return

    for num in range(start, N + 1):
        selected.append(num)
        backtrack(num + 1, depth + 1)
        selected.pop()

backtrack(1, 0)