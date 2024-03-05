class Student:
    def __init__(self, height, weight, number):
        self.height = height
        self.weight = weight
        self.number = number

    def __str__(self):
        return f'{self.height} {self.weight} {self.number}'

n = int(input())

arr = []

for number in range(1, n + 1):
    height, weight = tuple(map(int, input().split()))
    arr.append(Student(height, weight, number))

arr.sort(key=lambda x: (x.height, -x.weight))

for elem in arr:
    print(elem)