class Character:
    def __init__(self, ID: str, level: int):
        if 1 <= len(ID) <= 10:
            self.ID = ID

        if 1 <= level <= 30:
            self.level = level

    def __str__(self):
        return f'user {self.ID} lv {self.level}'

default_obj = Character('codetree', 10)

user_id, level = input().split()
level = int(level)

obj = Character(user_id, level)

print(default_obj)
print(obj)