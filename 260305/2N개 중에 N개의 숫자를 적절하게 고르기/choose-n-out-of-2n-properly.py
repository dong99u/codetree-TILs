n = int(input())
num = list(map(int, input().split()))

# Please write your code here.
INF = float('inf')
total_sum = sum(num)

memo = {}
def backtrack(idx, count, acc):
    state = (idx, count, acc)
    if state in memo:
        return memo[state]

    another = total_sum - acc
    if idx == n * 2:
        if count != n:
            return INF
        memo[state] = abs(acc - another)
        return memo[state]
    if count == n:
        memo[state] = abs(acc - another)
        return memo[state]

    result = INF
    for i in range(idx, n * 2):
        result = min(result, backtrack(i + 1, count + 1, acc + num[i]))
    memo[state] = result
    return result

answer = backtrack(0, 0, 0)

print(answer)