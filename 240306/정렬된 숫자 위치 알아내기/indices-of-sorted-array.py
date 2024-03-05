import sys
input = sys.stdin.readline

class Number:
    def __init__(self, number, index):
        self.number, self.index = number, index

n = int(input())
numbers = [
    Number(num, idx)
    for idx, num in enumerate(list(map(int, input().split())))
]
answer = [0] * n

numbers.sort(key=lambda x: (x.number, x.index))

for idx, number in enumerate(numbers):
    answer[number.index] = idx + 1

print(*answer)