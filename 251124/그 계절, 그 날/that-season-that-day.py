Y, M, D = map(int, input().split())

# Please write your code here.

def is_present(Y, M, D):
    d = get_last_day(Y, M)

    if M <= 12 and D <= d:
        return True
    else:
        return False

def is_leap(Y):
    return (Y % 4 == 0 and Y % 100 != 0) or (Y % 400 == 0)


def get_last_day(Y, M):
    if M == 2:
        if is_leap(Y):
            return 29
        else:
            return 28

    if M in [4, 6, 9, 11]:
        return 30
        
    return 31

if is_present(Y, M, D):
    if 3 <= M <= 5:
        print('Spring')
    elif 6 <= M <= 8:
        print('Summer')
    elif 9 <= M <= 11:
        print('Fall')
    else:
        print('Winter')
else:
    print(-1)