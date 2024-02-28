A = input()

answer = float("inf")


for _ in range(len(A)):
    encoded = ""
    count = 1
    curr_char = A[0]

    for target_char in A[1:]:
        if target_char == curr_char:
            count += 1
        else:
            encoded += curr_char
            encoded += str(count)

            curr_char = target_char
            count = 1

    encoded += curr_char
    encoded += str(count)

    answer = min(len(encoded), answer)

    A = A[-1] + A[:-1]

print(answer)