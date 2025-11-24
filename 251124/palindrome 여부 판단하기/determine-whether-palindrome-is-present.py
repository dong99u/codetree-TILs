A = input()

# Please write your code here.

def check(strs):
    n = len(strs)

    for i in range(n // 2):
        if strs[i] != strs[n - 1 - i]:
            return False
    return True

if check(A):
    print('Yes')
else:
    print('No')