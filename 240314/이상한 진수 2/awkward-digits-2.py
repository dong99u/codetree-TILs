def bin_to_dec(code: str):
    weight = 1
    dec = 0

    for binary in reversed(code):

        if int(binary) == 0:
            weight *= 2
            continue

        dec += weight * int(binary)
        weight *= 2

    return dec


binary = list(input())
answer = bin_to_dec("".join(binary))

for i in range(len(binary)):

    original = None
    if binary[i] == "0":
        original = "0"
        binary[i] = "1"

    else:
        original = "1"
        binary[i] = "0"

    answer = max(answer, bin_to_dec("".join(binary)))

    binary[i] = original

print(answer)