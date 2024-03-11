a, b = tuple(map(int, input().split()))
n = input()

# a진수를 10진수로 변환하는 함수
def a_to_dec(num: str, a: int) -> int:

    weight = 1
    decimal = 0

    for n in reversed(num):

        if int(n) == 0:
            weight *= a
            continue

        decimal += weight * int(n)
        weight *= a

    return decimal

def dec_to_b(num: int, b: int) -> str:
    
    results = []

    while True:

        if num < b:
            results.append(num)
            break
        
        results.append(num % b)
        num //= b
    
    results.reverse()
    return ''.join(list(map(str, results)))


result = a_to_dec(n, a)
result = dec_to_b(result, b)

print(result)