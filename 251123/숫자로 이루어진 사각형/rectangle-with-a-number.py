n = int(input())

# Please write your code here.

def print_number(n):
    number = 1
    for _ in range(n):
        for _ in range(n):
            print(number, end=' ')
            number += 1
            if number == 10:
                number = 1
            
        print()

print_number(n)