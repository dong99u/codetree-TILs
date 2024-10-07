from sortedcontainers import SortedDict

# 변수 선언 및 입력:
n = int(input())
words = [
    input() 
    for _ in range(n)
]

freq = SortedDict()

for word in words:
    if word not in freq:
        freq[word] = 1
    else:
        freq[word] += 1

# 순서대로 데이터를 순회합니다.
for word, cnt in freq.items():
    ratio = cnt / n * 100

    # 소숫점 4째짜리까지만 출력합니다.
    print(f"{word} {ratio:.4f}")