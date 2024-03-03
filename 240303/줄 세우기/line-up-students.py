class Student:
    def __init__(self, height: int, weight: int, number: int):
        self.height = height
        self.weight = weight
        self.number = number

N = int(input())

students = [
    Student(int(height), int(weight), int(idx)) for idx, (height, weight) in enumerate((input().split() for _ in range(N)), start = 1)
]

students.sort(key=lambda x: (-x.height, -x.weight, x.number))

for student in students:
    print(student.height, student.weight, student.number)