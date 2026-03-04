n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
x, y = 0, 0
mapper = {
    'E': 0,
    'W': 1,
    'S': 2,
    'N': 3
}
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for d, dist in zip(dir, dist):
    x += dx[mapper[d]] * dist
    y += dy[mapper[d]] * dist

print(x, y)