y = int(input())

# Please write your code here.

def check(y):
    if y % 4 == 0:
        if y % 100 == 0 and y % 400 != 0:
            return False
        else:
            return True
    return False

if check(y):
    print('true')
else:
    print('false')
    