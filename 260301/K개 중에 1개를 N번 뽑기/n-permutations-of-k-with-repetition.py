K, N = map(int, input().split())

# Please write your code here.
def backtrack(selected, depth):
    # 기저 조건
    if depth == N:
        print(*selected)
        return

    for i in range(1, K + 1):
        backtrack(selected + [i], depth + 1)

backtrack([], 0)