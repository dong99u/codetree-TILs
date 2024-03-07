digits = input()

decimal = 0
weight = 1

for digit in reversed(digits):

    if int(digit) == 1:
        decimal += weight

    weight *= 2

print(decimal)