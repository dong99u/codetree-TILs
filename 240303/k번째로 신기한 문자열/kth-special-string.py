import sys
input = sys.stdin.readline

n, k, T = input().split()
n = int(n)
k = int(k)

words = [
    input().strip()
    for _ in range(n)
]

def check_T(words: list, T: str) -> list:
    result = []

    for word in words:
        if T in word:
            result.append(word)

    result.sort()

    return result

result = check_T(words, T)


print(result[k - 1])