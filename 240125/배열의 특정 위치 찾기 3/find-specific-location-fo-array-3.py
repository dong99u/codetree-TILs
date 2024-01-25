num_list = list(map(int, input().split()))

sum_val = 0
for idx, val in enumerate(num_list):
    if val != 0:
        continue
    
    sum_val = sum(num_list[idx - 3 : idx])
    break

print(sum_val)