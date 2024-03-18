import sys
INT_MIN = -sys.maxsize

n = int(input())

arr = [
    int(input()) for _ in range(n)
]

# 캐리가 발생했는지 체크하는 함수
# 캐리 발생하면 return True
# 발생하지 않으면 return False
def is_carry(num1: str, num2: str, num3: str) -> bool:
    num1, num2, num3 = align_number(num1, num2, num3)
    for a, b, c in zip(num1, num2, num3):
        if int(a) + int(b) + int(c) >= 10:
            return True
    
    return False

def align_number(num1, num2, num3):
    max_num = max(len(num1), len(num2), len(num3))

    num1 = num1[::-1]
    num2 = num2[::-1]
    num3 = num3[::-1]

    for _ in range(max_num - len(num1)):
        num1 += "0"
    for _ in range(max_num - len(num2)):
        num2 += "0"
    for _ in range(max_num - len(num3)):
        num3 += "0"

    return num1, num2, num3

answer = INT_MIN
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):

            num1 = str(arr[i])
            num2 = str(arr[j])
            num3 = str(arr[k])

            if is_carry(num1, num2, num3):
                continue
            else:
                val = arr[i] + arr[j] + arr[k]
                answer = max(answer, val)


            
            
print(answer)