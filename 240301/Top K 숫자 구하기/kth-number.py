n, k = tuple(map(int, input().split()))

l = list(map(int, input().split()))

l.sort()

print(l[k - 1])