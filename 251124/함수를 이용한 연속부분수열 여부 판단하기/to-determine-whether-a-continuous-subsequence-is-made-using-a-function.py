n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.

def check(a, b):
    n = len(a)
    m = len(b)
    
    for i in range(n - m + 1):
        lst = []
        for j in range(i, i + m):
            lst.append(a[j])
        if is_same(lst, b):
            return True
    return False
            
def is_same(lst1, lst2):
    for elem1, elem2 in zip(lst1, lst2):
        if elem1 != elem2:
            return False
    return True

if check(a, b):
    print('Yes')
else:
    print('No')