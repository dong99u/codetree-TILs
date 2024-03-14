n = int(input())

houses = list(map(int, input().split()))

distances = [0] * n

for house_number in range(n):

    distance_sum = 0
    for i in range(n):
        distance_sum += abs(house_number - i) * houses[i]

    distances[house_number] = distance_sum

print(min(distances))