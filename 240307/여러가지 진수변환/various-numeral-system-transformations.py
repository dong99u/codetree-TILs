n, b = tuple(map(int, input().split()))


digits = []

while True:

    if n < b:
        digits.append(n % b)
        break

    digits.append(n % b)
    n //= b

for elem in reversed(digits):
    print(elem, end='')