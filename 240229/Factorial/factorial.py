def factorial(n):
    if n == 0 or n == 1:
        return 1
    
    return factorial(n - 1) * n


result = factorial(int(input()))

print(result)