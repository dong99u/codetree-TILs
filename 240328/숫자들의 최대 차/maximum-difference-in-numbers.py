n, k = map(int, input().split())
MAX_NUM = 10000
nums = [
    int(input())
    for _ in range(n)
]

answer = 0

def count_num(start, end):
    cnt = 0
    for num in nums:
        if start <= num <= end:
            cnt += 1

    return cnt

for i in range(1, MAX_NUM + 1):
    
    cnt = count_num(i, i + k)

    answer = max(answer, cnt)

print(answer)