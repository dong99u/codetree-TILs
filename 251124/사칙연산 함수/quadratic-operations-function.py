a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.

def add(a, c):
    return a + c

def minus(a, c):
    return a - c

def multi(a, c):
    return a * c

def devide(a, c):
    return a // c

if o in '+-/*':
    if o == '+':
        print(a, o, c, '=', add(a, c))
    elif o == '-':
        print(a, o, c, '=', minus(a, c))
    elif o == '*':
        print(a, o, c, '=', multi(a, c))
    else:
        print(a, o, c, '=', devide(a, c))
else:
    print(False)