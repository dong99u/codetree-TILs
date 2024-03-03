class Secret:
    def __init__(self, code, location, time):
        self.code = code
        self.location = location
        self.time = time

    def __str__(self):
        return '''secret code : {}
meeting point : {}
time : {}'''.format(self.code, self.location, self.time)
    
code, location, time = input().split()

obj = Secret(code, location, time)

print(obj)