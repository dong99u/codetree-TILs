n = int(input())

digits = []

while True:
    if n < 2:
        digits.append(n % 2)
        break

    digits.append(n % 2)
    n //= 2

for elem in reversed(digits):
    print(elem, end='')