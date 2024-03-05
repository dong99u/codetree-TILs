class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def __str__(self):
        return f'{self.name} {self.height} {self.weight}'

l = []

for _ in range(5):
    name, height, weight = input().split()
    height = int(height)
    weight = float(weight)

    l.append(Person(name, height, weight))

l.sort(key=lambda x: x.name)

print('name')
for elem in l:
    print(elem)

l.sort(key=lambda x: -x.height)

print() 

print('height')
for elem in l:
    print(elem)