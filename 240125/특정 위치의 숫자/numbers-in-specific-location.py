num_list = list(map(int, input().split()))

sum_val = 0

for idx, val in enumerate(num_list):
    if idx == 2 or idx == 4 or idx == 9:
        sum_val += val

print(sum_val)