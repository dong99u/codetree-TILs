n = int(input())
l = list(map(int, input().split()))

def gcd(a, b):

    if b == 0:
        return a

    else:
        return gcd(b, a % b)

def lcm(a, b):
    return a * b / gcd(a, b)


def f(n):        
    if n == 1:
        return lcm(l[0], l[1])
    if n == 0:
        return l[0]

    return lcm(f(n - 1), l[n])

result = int(f(n - 1))

print(result)