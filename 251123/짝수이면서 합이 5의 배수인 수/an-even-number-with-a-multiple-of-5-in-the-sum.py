n = int(input())

# Please write your code here.

def check(n):
    return n % 2 == 0 and sum([int(i) for i in str(n)]) % 5 == 0

if check(n):
    print('Yes')
else:
    print('No')