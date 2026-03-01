import re

expression = input()

# 1. 토큰화: 알파벳과 연산자 분리
tokens = [t for t in re.split(r'([a-f])', expression) if t]

# 2. 고유 알파벳 추출
alphabets = sorted(set(c for c in expression if c.isalpha()))

# 3. 연산자 매핑
ops = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
}

# 4. 왼→오 순서대로 계산
def calculate(mapping):
    result = mapping[tokens[0]]  # 첫 번째 알파벳
    for i in range(1, len(tokens), 2):  # 홀수: 연산자, 짝수: 알파벳
        result = ops[tokens[i]](result, mapping[tokens[i + 1]])
    return result

# 5. 백트래킹: 각 알파벳에 1~4 배정
mapping = {}
max_result = -1e9

def dfs(depth):
    global max_result

    if depth == len(alphabets):
        max_result = max(max_result, calculate(mapping))
        return

    for num in range(1, 5):
        mapping[alphabets[depth]] = num
        dfs(depth + 1)
        del mapping[alphabets[depth]]

dfs(0)
print(max_result)