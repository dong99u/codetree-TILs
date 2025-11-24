# 변수 선언 및 입력
m, d = tuple(map(int, input().split()))


# 윤년이 아닐 때 m번째 달의 마지막 날을 반환하는 함수를 작성합니다.
def last_day_number(m):
    if m == 2:
        return 28
    if m == 4 or m == 6 or m == 9 or m == 11:
        return 30
    
    return 31


# 윤년이 아닐 때 m월 d일이 존재하는지 여부를 확인하는 함수를 작성합니다.
def judge_day(m, d):
    if m <= 12 and d <= last_day_number(m):
        return True
    
    return False

    
if judge_day(m, d):
    print("Yes")
else:
    print("No")
