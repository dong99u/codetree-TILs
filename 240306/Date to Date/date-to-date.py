m1, d1, m2, d2 = tuple(map(int, input().split()))

#                  1   2   3   4   5   6   7   8   9  10  11  12
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

print((sum(num_of_days[:m2]) + d2) - (sum(num_of_days[:m1]) + d1) + 1)