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

def is_sum_even(n):
    result = 0
    while n > 0:
        result += n % 10
        n //= 10
    return result % 2 == 0

def check(n):
    return is_prime(n) and is_sum_even(n)

answer = 0
for n in range(a, b + 1):
    if check(n):
        answer += 1

print(answer)