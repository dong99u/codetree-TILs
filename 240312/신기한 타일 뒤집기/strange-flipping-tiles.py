from enum import Enum


class Color:
    BLACK = "Black"
    WHITE = "White"
    GREY = "Grey"


class Tiles:
    def __init__(self, size: int):
        self.__size = size
        self.__tiles = [Tile() for _ in range(size)]

    def flip(self, start_index: int, end_index: int, color: Color):

        for i in range(start_index, end_index + 1):
            self.__tiles[i].color = color

    def count(self):
        cnt_black = 0
        cnt_white = 0

        for i in range(self.__size):
            if self.__tiles[i].color == Color.BLACK:
                cnt_black += 1
            else:
                cnt_white += 1

        return (cnt_white, cnt_black)


class Tile:
    def __init__(self, color: Color = Color.GREY):
        self.__color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value


# 명령의 개수
n = int(input())

curr_index = 0
max_index = -float("inf")
min_index = float("inf")

orders = []
for _ in range(n):
    distance, direction = input().split()
    distance = int(distance)

    if direction == "R":
        section_left = curr_index
        section_right = curr_index + distance - 1

        orders.append((section_left, section_right, Color.BLACK))

        max_index = max(max_index, section_right)

        curr_index = section_right

    elif direction == "L":
        section_left = curr_index - distance + 1
        section_right = curr_index

        orders.append((section_left, section_right, Color.WHITE))

        min_index = min(min_index, section_left)

        curr_index = section_left


total = max_index - min_index + 1
OFFSET = abs(min_index)

tiles = Tiles(total)

for order in orders:
    start_index = order[0]
    end_index = order[1]
    color = order[2]

    tiles.flip(start_index + OFFSET, end_index + OFFSET, color)

answer_white, answer_black = tiles.count()

print(answer_white, answer_black)