n = int(input())

l = [
    input()
    for _ in range(n)
]

l.sort()

for elem in l:
    print(elem)