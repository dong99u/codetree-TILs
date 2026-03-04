n = int(input())
num = list(map(int, input().split()))

# Please write your code here.
def backtrack(count, curr):
    if curr >= n - 1:
        return count
    max_jump = num[curr]
    result = 1e9
    for jump in range(1, max_jump + 1):
        result = min(result, backtrack(count + 1, curr + jump))

    return result

answer = backtrack(0, 0)

print(answer if answer != 1e9 else -1)