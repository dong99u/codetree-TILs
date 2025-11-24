a, b = map(int, input().split())

# Please write your code here.

def check(n):
    return n % 2 == 0 and n // 10 == 5 and (n % 3 == 0 and n % 9 != 0)

answer = 0
for n in range(a, b + 1):
    if check(n):
        answer += 1

print(answer)