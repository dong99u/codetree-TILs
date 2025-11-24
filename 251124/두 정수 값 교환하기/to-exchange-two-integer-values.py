n, m = map(int, input().split())

# Please write your code here.

def swap(n, m):
    n, m = m, n
    return n, m

n, m = swap(n, m)

print(n, m)