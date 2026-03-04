n = int(input())
num = list(map(int, input().split()))

# Please write your code here.
INF = float('inf')
total_sum = sum(num)

def backtrack(idx, count, acc):
    another = total_sum - acc
    if idx == n * 2:
        if count != n:
            return INF
        return abs(acc - another)
    if count == n:
        return abs(acc - another)

    result = INF
    for i in range(idx, n * 2):
        result = min(result, backtrack(i + 1, count + 1, acc + num[i]))

    return result

answer = backtrack(0, 0, 0)

print(answer)