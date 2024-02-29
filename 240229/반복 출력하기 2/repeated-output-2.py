N = int(input())

def print_hello(n):
    if n == 0:
        return
    
    print("HelloWorld")
    print_hello(n - 1)

print_hello(N)