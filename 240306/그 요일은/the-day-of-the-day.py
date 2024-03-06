m1, d1, m2, d2 = tuple(map(int, input().split()))

#                  1   2   3   4   5   6   7   8   9  10  11  12
num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

arr = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

days = (sum(num_of_days[:m2]) + d2) - (sum(num_of_days[:m1]) + d1)

day = input()

answer = days // 7

if days % 7 >= arr.index(day):
    answer += 1

print(answer)