n = int(input())

def f(n):
    
    if n == 1:
        return 2
    if n== 2:
        return 4
    
    return (f(n - 2) * f(n - 1)) % 100

result = f(n)

print(result)