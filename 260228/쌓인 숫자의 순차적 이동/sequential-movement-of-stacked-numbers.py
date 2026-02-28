from collections import defaultdict

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
move_nums = list(map(int, input().split()))

# Please write your code here.

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def get_next_coord(x, y):
    mx, my = None, None
    max_val = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if not in_range(nx, ny):
            continue

        for num in nums[nx][ny]:
            if max_val < num:
                max_val = num
                mx, my = nx, ny

    return mx, my

def move(num):
    for x in range(n):
        for y in range(n):
            if move_num in nums[x][y]:
                idx = nums[x][y].index(move_num)
                nx, ny = get_next_coord(x, y)

                if nx is None and ny is None:
                    return

                nums[nx][ny].extend(nums[x][y][idx:])
                nums[x][y][idx:] = []
                return


dxs = [1, 1, 0, -1, -1, -1, 0, 1]
dys = [0, 1, 1, 1, 0, -1, -1, -1]

nums = [
    [
        [] for _ in range(n)
    ]
    for _ in range(n)
]

for x in range(n):
    for y in range(n):
        nums[x][y].append(grid[x][y])

for move_num in move_nums:
    move(move_num)

for row in nums:
    for elem in row:
        if len(elem) == 0:
            print(None)
        else:
            print(*reversed(elem))


