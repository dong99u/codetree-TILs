class Agent:
    def __init__(self, code_name, grade: int):
        self.code_name = code_name
        self.grade = grade

    def __str__(self):
        return f'{self.code_name} {self.grade}'

agent_list = []

for _ in range(5):
    code_name, grade = input().split()
    grade = int(grade)
    agent_list.append(
        Agent(code_name, grade)
    )

agent_list.sort(key=lambda x: x.grade)

print(agent_list[0])