# 변수 선언 및 입력:
n, k = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

count = dict()

ans = 0
# 배열을 앞에서부터 순회하며 쌍을 만들어줍니다.
for elem in arr:
    diff = k - elem
    # 가능한 모든 쌍의 수를 세어줍니다.
    if diff in count:
        ans += count[diff]

    # 현재 숫자의 개수를 하나 증가시켜줍니다.
    if elem in count:
        count[elem] += 1
    else:
        count[elem] = 1

print(ans)