import sys

INF = float('inf')
input = sys.stdin.readline

n, m = map(int, input().split())

points = []

select = []

result = INF
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))


def get_max_distance():
    max_dist = -1

    for point1 in range(len(select)):
        for point2 in range(point1 + 1, len(select)):

            if select[point1] == 0 or select[point2] == 0:
                continue
            else:
                x1, y1 = points[point1]
                x2, y2 = points[point2]

                distance = (((x2 - x1) ** 2) + ((y2 - y1) ** 2))
                max_dist = max(max_dist, distance)

    return max_dist

def back_track(curr_num, cnt):
    global result

    if curr_num >= n + 1:
        return

    # m 개의 점을 선택했다면
    if cnt >= m:
        max_dist = get_max_distance()
        result = min(result, max_dist)
        return

    select.append(1)
    back_track(curr_num + 1, cnt + 1)
    select.pop()

    select.append(0)
    back_track(curr_num + 1, cnt)
    select.pop()


back_track(0, 0)
print(result)