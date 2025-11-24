a, b = map(int, input().split())

# Please write your code here.
def check(num):
    return num % 3 == 0 or check_369(num)

def check_369(num):
    while num > 0:
        if num % 10 == 3 or num % 10 == 6 or num % 10 == 9:
            return True
        num //= 10
    return False

answer = 0
for num in range(a, b + 1):
    if check(num):
        answer += 1

print(answer)
