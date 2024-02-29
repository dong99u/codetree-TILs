def print_num(n):
    if n == 0:
        return
    
    print(n, end=' ')
    print_num(n - 1)
    print(n, end=' ')


N = int(input())
print_num(N)