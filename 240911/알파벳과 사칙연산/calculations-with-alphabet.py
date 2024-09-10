from itertools import product


def evaluate(expression, values):
    tokens = []
    for char in expression:
        if char.isalpha():
            tokens.append(values[char])
        else:
            tokens.append(char)

    result = int(tokens[0])
    for i in range(1, len(tokens), 2):
        op, value = tokens[i], int(tokens[i + 1])
        if op == '+':
            result += value
        elif op == '-':
            result -= value
        elif op == '*':
            result *= value

    return result


def maximize_expression(expression):
    alphabet = set(char for char in expression if char.isalpha())
    max_result = float('-inf')

    for combination in product(range(1, 5), repeat=len(alphabet)):
        values = dict(zip(alphabet, combination))
        result = evaluate(expression, values)
        max_result = max(max_result, result)

    return max_result


# 입력 받기
expression = input().strip()

# 결과 계산 및 출력
result = maximize_expression(expression)
print(result)