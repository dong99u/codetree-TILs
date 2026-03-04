from collections import defaultdict

n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
memo = defaultdict(int)
def backtrack(idx, curr, count):
    state = (idx, count)
    if state in memo:
        return memo[state]
    if count == m:
        memo[state] = curr
        return curr
    if idx == n:
        return count

    result = max(backtrack(idx + 1, curr ^ A[idx], count + 1), backtrack(idx + 1, curr, count))

    memo[state] = result

    return result


print(backtrack(0, 0, 0))