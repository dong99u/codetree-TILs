n, m, k = map(int, input().split()) # 4, 6, 3
nums = list(map(int, input().split())) # 2, 4, 2, 4

# Please write your code here.
def backtrack(depth, point, state):
    if depth == n:
        return point

    max_result = 0
    for i in range(k):
        if state[i] == m - 1:
            backtrack(depth + 1, point, state)
            continue

        prev = state[i]
        nxt = prev + nums[depth]

        if nxt >= m - 1:
            state[i] = m - 1
            max_result = max(max_result, backtrack(depth + 1, point + 1, state))
        else:
            state[i] = nxt
            max_result = max(max_result, backtrack(depth + 1, point, state))

        state[i] = prev

    return max_result

answer = backtrack(0, 0, [0] * k)

print(answer)