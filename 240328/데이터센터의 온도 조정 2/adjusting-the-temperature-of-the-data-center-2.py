n, c, g, h = map(int, input().split())

prefs = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

def get_workload(curr_temp, ta, tb):
    global c, g, b

    if curr_temp < ta: return c
    elif ta <= curr_temp <= tb: return g
    else: return h

answer = 0
for curr_temp in range(1000 + 1):
    works = 0
    for ta, tb in prefs:
        works += get_workload(curr_temp, ta, tb)

    answer = max(answer, works)

print(answer)