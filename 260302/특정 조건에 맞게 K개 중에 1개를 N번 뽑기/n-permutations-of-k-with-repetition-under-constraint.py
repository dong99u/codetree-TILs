K, N = map(int, input().split())

# Please write your code here.
def backtrack(depth, selected):
    if depth == N:
        print(*selected)
        return

    for i in range(1, K + 1):
        if len(selected) >= 2 and selected[-2] == selected[-1] == i:
            continue

        backtrack(depth + 1, selected + [i])

backtrack(0, [])