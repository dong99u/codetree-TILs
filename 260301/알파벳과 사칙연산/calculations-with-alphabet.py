import re

expression = input()
n = len(expression)
operators = [t for t in re.split(r'[a-f]', expression) if t]

mapper = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
}

def backtrack(depth, result, max_result):
    if depth == ((n + 1) // 2) - 1:
        return result

    for i in range(1, 4 + 1):
        max_result = max(max_result, backtrack(depth + 1, mapper[operators[depth]](result, i), max_result))

    return max_result

answer = -1e9
for i in range(1, 4 + 1):
    answer = max(answer, backtrack(0, i, answer))

print(answer)

