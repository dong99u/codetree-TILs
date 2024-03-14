import sys
input = sys.stdin.readline

n = int(input())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

def sum_coins(x, y):
    coin = 0
    for i in range(3):
        coin += grid[x][y + i]
    
    return coin

answer = 0
for x in range(n):
    for y in range(n):

        if y + 3 > n:
            continue

        answer = max(answer, sum_coins(x, y))

        
print(answer)