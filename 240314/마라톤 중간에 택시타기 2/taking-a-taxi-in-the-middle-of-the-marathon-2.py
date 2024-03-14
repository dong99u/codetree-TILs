import sys

INT_MAX = sys.maxsize

# 두 점 사이의 맨하탄 거리를 구하는 함수
# point1 -> (x1, y1)
# point2 -> (x2, y2)
def get_distance(x1, y1, x2, y2) -> int:
    return abs(x1 - x2) + abs(y1 - y2)

n = int(input())

course_positions = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

answer = INT_MAX
# 1번과 n번 코스를 제외한 나머지 2번 ~ n - 1 코스를 선택
for excepted_course_number in range(1, n - 1):
    distance = 0
    prev_check_point = 0

    for i in range(1, n):
        if i == excepted_course_number:
            continue

        distance += get_distance(*course_positions[prev_check_point], *course_positions[i])
        prev_check_point = i

    answer = min(answer, distance)

print(answer)