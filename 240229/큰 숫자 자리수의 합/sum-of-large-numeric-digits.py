a, b, c = tuple(map(int, input().split()))

num = a * b * c

def get_sum(num):
    if num < 10:
        return num
    
    return get_sum(num // 10) + (num % 10)

result = get_sum(num)

print(result)