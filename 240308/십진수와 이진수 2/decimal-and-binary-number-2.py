def binary_to_decimal(n: str) -> int:
    decimal = 0
    weight = 1

    for digit in reversed(n):

        if int(digit) == 0:
            weight *= 2
            continue

        decimal += int(digit) * weight
        weight *= 2

    return decimal


def decimal_to_binary(n: int) -> str:

    digits = []

    while True:

        if n < 2:
            digits.append(n % 2)
            break

        digits.append(n % 2)
        n //= 2

    result = "".join(list(map(str, digits)))

    return result[::-1]


n = input()

decimal = binary_to_decimal(n)

decimal *= 17

answer = decimal_to_binary(decimal)

print(answer)