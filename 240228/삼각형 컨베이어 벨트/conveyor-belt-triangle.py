n, t = tuple(map(int, input().split()))

l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
l3 = list(map(int, input().split()))

sum_list = l1 + l2 + l3

for _ in range(t):
    temp = sum_list.pop(-1)
    sum_list.insert(0, temp)
    
print(*sum_list[:n])
print(*sum_list[n:2*n])
print(*sum_list[2*n:])