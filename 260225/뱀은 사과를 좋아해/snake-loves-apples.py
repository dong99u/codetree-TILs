from collections import deque

HEAD = 0
TAIL = -1

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def move(d):
    dx, dy = directions[d]  # 다음 방향
    head_x, head_y = snake[HEAD]  # 현재 head 위치

    new_head_x, new_head_y = head_x + dx, head_y + dy  # 새로운 머리의 위치

    if not in_range(new_head_x, new_head_y):
        return False

    eating = False
    if apples[new_head_x][new_head_y] == 1:
        eating = True

    if not eating:
        tail_x, tail_y = snake.pop()
        snake_set.remove((tail_x, tail_y))
    else:
        apples[new_head_x][new_head_y] = 0

    new_head = (new_head_x, new_head_y)
    if new_head in snake_set:
        return False

    snake.appendleft(new_head)
    snake_set.add(new_head)



    return True



n, m, k = map(int, input().split())

apples = [
    [0] * n
    for _ in range(n)
]

for _ in range(m):
    xi, yi = map(int, input().split())

    apples[xi - 1][yi - 1] = 1

d, p = [], []
for _ in range(k):
    di, pi = input().split()
    d.append(di)
    p.append(int(pi))

# Please write your code here.

cx, cy = 0, 0
snake = deque([(cx, cy)])
snake_set = {(cx, cy)}

directions = {
    'L': (0, -1),
    'R': (0, 1),
    'U': (-1, 0),
    'D': (1, 0)
}

over = False
time = 0

for di, pi in zip(d, p):
    for _ in range(pi):
        time += 1
        if not move(di):
            over = True
            break


    if over:
        break

print(time)