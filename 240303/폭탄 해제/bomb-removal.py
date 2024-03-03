class Bomb:
    def __init__(self, code: str, color: str, second: int):
        self.code = code
        self.color = color  
        self.second = second

    def __str__(self):
        return '''code : {}
color : {}
second : {}'''.format(self.code, self.color, self.second)

code, color, second = input().split()

second = int(second)

obj = Bomb(code, color, second)

print(obj)