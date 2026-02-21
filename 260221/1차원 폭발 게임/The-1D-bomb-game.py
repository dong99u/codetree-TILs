n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)]

# Please write your code here.
while True:
    count = 1
    temp = []
    changed = False

    if not numbers:
        break

    for i in range(1, len(numbers)):
        if numbers[i - 1] == numbers[i]:
            count += 1
        else:
            if count < m:
                temp += [numbers[i - 1]] * count
            else:
                changed = True
            count = 1

    if count < m:
        temp += [numbers[len(numbers) - 1]] * count
    else:
        changed = True

    numbers = temp

    if not changed:
        break

print(len(numbers))
for elem in numbers:
    print(elem)