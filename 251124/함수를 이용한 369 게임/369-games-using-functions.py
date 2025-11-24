a, b = map(int, input().split())

# Please write your code here.
def check(num):
    return num % 3 == 0 or check_369(num)

def check_369(num):
    num_str = str(num)
    for elem in num_str:
        if elem in '369':
            return True
    return False

answer = 0
for num in range(a, b + 1):
    if check(num):
        answer += 1

print(answer)
