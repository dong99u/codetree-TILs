num_list = list(map(int, input().split()))

even_sum = sum(num_list[1::2])
odd_sum = sum(num_list[::2])

print(abs(even_sum - odd_sum))