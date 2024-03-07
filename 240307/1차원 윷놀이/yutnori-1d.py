import sys

input = sys.stdin.readline

n, m, k = tuple(map(int, input().split()))
turns = list(map(int, input().split()))

selected_horse_numbers = []

answer = 0


# 총 k 개의 턴
# curr_num 번째 턴에 움직일 말
def choose(curr_num):

    # 종료 조건
    if curr_num == n + 1:
        calculate_point()
        return

    # 진행 조건
    for i in range(1, k + 1):
        selected_horse_numbers.append(i)
        choose(curr_num + 1)
        selected_horse_numbers.pop()


def calculate_point():
    global answer
    point = 0

    distances = [0] * k
    for idx, horse_number in enumerate(selected_horse_numbers):

        distances[horse_number - 1] += turns[idx]

    for distance in distances:
        if distance >= m:
            point += 1

    answer = max(point, answer)


choose(1)
print(answer)