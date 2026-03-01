n = int(input())
x1, x2 = [], []

for _ in range(n):
    a, b = map(int, input().split())
    x1.append(a)
    x2.append(b)

# Please write your code here.
length_count = [0] * 1001

def backtrack(idx, count, length_count):
    if idx == n:
        return count
    result = 0
    l, r = x1[idx], x2[idx]
    if all(i == 0 for i in length_count[l : r + 1]):
        length_count[l : r + 1] = [1] * (r - l + 1)
        result = max(result, backtrack(idx + 1, count + 1, length_count))
        length_count[l: r + 1] = [0] * (r - l + 1)
    result = max(result, backtrack(idx + 1, count, length_count))

    return result

answer = backtrack(0, 0, length_count)
print(answer)