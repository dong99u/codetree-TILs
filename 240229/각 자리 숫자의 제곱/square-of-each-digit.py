N = int(input())

def get_sum(n):
    if n < 10:
        return n ** 2
    
    return get_sum(n // 10) + ((n % 10) ** 2)

print(get_sum(N))