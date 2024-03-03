# 클래스 선언
class Student:
    def __init__(self, name, height, weight):
        self.name, self.height, self.weight = name, height, weight


# 변수 선언 및 입력
n = int(input())
students = []
for _ in range(n):
    name, height, weight = tuple(input().split())
    students.append(Student(name, int(height), int(weight)))

# Custom Comparator를 활용한 정렬
students.sort(key = lambda x: x.height)

# 출력
for student in students:
    print(student.name, student.height, student.weight)