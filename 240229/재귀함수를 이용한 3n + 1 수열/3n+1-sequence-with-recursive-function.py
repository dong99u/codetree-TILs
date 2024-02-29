n = int(input())

def f(n, cnt):
    if n == 1:
        return cnt

    if n % 2 == 0:
        return f(n // 2, cnt + 1)
    else:
        return f(3*n + 1, cnt + 1)

result = f(n, 0)

print(result)