n = int(input())

# Please write your code here.
selected = []

def valid(depth):
    for length in range(1, (depth // 2) + 1):
        if selected[-1 : -1 - length : -1] == selected[-1 - length : -1 - length * 2 : -1]:
            return False
    return True

def backtrack(depth):
    if not valid(depth):
        return
    if depth == n:
        return selected

    for num in range(4, 6 + 1):
        selected.append(num)
        result = backtrack(depth + 1)
        if result is not None:
            return result
        selected.pop()


answer = ''.join(map(str, backtrack(0)))

print(answer)