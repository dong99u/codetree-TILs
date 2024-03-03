class Agent:
    def __init__(self, code_name, grade: int):
        self.code_name = code_name
        self.grade = grade

    def __str__(self):
        return f'{self.code_name} {self.grade}'

# 리스트 컴프리헨션을 사용하여 agent_list 초기화
agent_list = [Agent(code_name, int(grade)) for code_name, grade in (input().split() for _ in range(5))]

agent_list.sort(key=lambda x: x.grade)

print(agent_list[0])