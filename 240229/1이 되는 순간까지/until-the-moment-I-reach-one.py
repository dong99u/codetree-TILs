N = int(input())
def f(n, cnt):
    if n == 1:
        return cnt

    # if 짝수
    if n % 2 == 0:
        return f(n // 2, cnt + 1)
    else:
        return f(n // 3, cnt + 1)

result = f(N, 0)

print(result)