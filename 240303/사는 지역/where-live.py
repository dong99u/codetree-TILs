class Person:
    def __init__(self, name, address, city):
        self.name = name
        self.address = address
        self.city = city

# n을 입력받음
n = int(input())

# Person 객체를 담을 리스트 초기화
people = []

# n명의 자료를 입력받아 Person 객체를 생성하고 리스트에 추가
for _ in range(n):
    name, address, city = input().split()
    people.append(Person(name, address, city))

# 이름의 사전순으로 가장 느린 사람을 찾기
latest_person = max(people, key=lambda person: person.name)

# 해당 사람의 자료 출력
print(f'name {latest_person.name}')
print(f'addr {latest_person.address}')
print(f'city {latest_person.city}')