n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.

def backtrack(idx, curr, count):
    if count == m:
        return curr
    if idx == n:
        return count
    return max(backtrack(idx + 1, curr ^ A[idx], count + 1), backtrack(idx + 1, curr, count))

print(backtrack(0, 0, 0))