num_list = list(map(int, input().split()))

even_sum = sum(num_list[1::2])

lst = num_list[2::3]
avg = sum(lst) / len(lst)

print(even_sum, avg)