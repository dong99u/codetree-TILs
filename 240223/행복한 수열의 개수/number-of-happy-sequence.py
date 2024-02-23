# n: 격자의 크기 n x n
# m: 연속해야하는 숫자의 크기

answer = 0

n, m = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 각 행이 행복한 수열인지 확인하는 함수
def happy_row():
    global answer
    for row in grid:
        if sequence_check(row):
            answer += 1

# 각 열이 행복한 수열인지 확인하는 함수
def happy_col():
    global answer
    columns = list(zip(*grid))
    for column in columns:
        if sequence_check(column):
            answer += 1
        


# m개 이상 연속한지 확인하는 함수
# m개 이상 연속하면 return True
def sequence_check(sequence: list) -> bool:
    count = 1
    max_count = 1
    for i in range(1, len(sequence)):
        if sequence[i - 1] == sequence[i]:
            count += 1
        else:
            count = 1
        
        max_count = max(count, max_count)
    
    return max_count >= m

happy_row()
happy_col()

print(answer)