n, m, k = map(int, input().split()) # 4, 6, 3
nums = list(map(int, input().split())) # 2, 4, 2, 4

# Please write your code here.
def backtrack(depth, state):
    if depth == n:
        return 0

    best = 0
    move = nums[depth]

    for i in range(k):
        if state[i] == m - 1:
            # 변화 없음, 이번 턴 점수 0
            best = max(best, backtrack(depth + 1, state))
            continue

        prev = state[i]
        nxt = prev + move

        if nxt >= m - 1:
            state[i] = m - 1
            best = max(best, 1 + backtrack(depth + 1, state))
        else:
            state[i] = nxt
            best = max(best, backtrack(depth + 1, state))

        state[i] = prev

    return best

answer = backtrack(0, [0] * k)
print(answer)