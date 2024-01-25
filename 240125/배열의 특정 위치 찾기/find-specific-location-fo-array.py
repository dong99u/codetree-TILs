num_list = list(map(int, input().split()))

even_sum = sum(num_list[1::2])

lst = num_list[2::3]
avg = round(sum(lst) / len(lst), 1)

print(even_sum, avg)