import math

a, b = map(int, input().split())

# Please write your code here.

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True

answer = 0
for n in range(a, b + 1):
    if is_prime(n):
        answer += 1

print(answer)