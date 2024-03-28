n = int(input())

arr = input()

answer = 0

for seat_num in range(n):

    if arr[seat_num] == "1":
        continue

    if arr[seat_num] == "0":
        d1 = d2 = float('inf')

        for i in range(seat_num - 1, -1, -1):
            if arr[i] == "1":
                d1 = seat_num - i
                break

        for i in range(seat_num + 1, n):
            if arr[i] == "1":
                d2 = i - seat_num
                break

        min_dist = min(d1, d2)

        answer = max(answer, min_dist)

print(answer)