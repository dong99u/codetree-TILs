class Tile:
    def __init__(self, color=None, white_time=0, black_time=0):
        self.__color = color
        self.__white_time = white_time
        self.__black_time = black_time

    # Getter
    @property
    def color(self):
        return self.__color

    @property
    def white_time(self):
        return self.__white_time

    @property
    def black_time(self):
        return self.__black_time

    # Setter
    @color.setter
    def color(self, value):
        self.__color = value

    @white_time.setter
    def white_time(self, value):
        self.__white_time = value

    @black_time.setter
    def black_time(self, value):
        self.__black_time = value

    def __turn_grey(self):
        if self.__white_time >= 2 and self.__black_time >= 2:
            self.__color = "Grey"

    # 새로운 메서드
    def increment_white_time(self):
        self.__white_time += 1
        self.__turn_grey()

    def increment_black_time(self):
        self.__black_time += 1
        self.__turn_grey()


def color(start_index: int, end_index: int, value: str):
    global tiles

    if value == "Black":
        for i in range(start_index, end_index + 1):
            tiles[i].color = "Black"
            tiles[i].increment_black_time()

    elif value == "White":
        for i in range(start_index, end_index + 1):
            tiles[i].color = "White"
            tiles[i].increment_white_time()


# 명령의 개수
n = int(input())

orders = []

# 현재 위치
curr_index = 0
min_index = float("inf")
max_index = -float("inf")

for _ in range(n):
    distance, direction = input().split()
    distance = int(distance)

    if direction == "R":
        section_left = curr_index
        section_right = curr_index + distance - 1

        max_index = max(max_index, section_right)

        orders.append((section_left, section_right, "Black"))
        curr_index = section_right

    elif direction == "L":
        section_left = curr_index - distance + 1
        section_right = curr_index

        min_index = min(min_index, section_left)

        orders.append((section_left, section_right, "White"))
        curr_index = section_left


total = max_index - min_index + 1

tiles = [Tile() for _ in range(total)]

OFFSET = abs(min_index)


for order in orders:
    start_index = order[0]
    end_index = order[1]
    color_value = order[2]

    color(start_index + OFFSET, end_index + OFFSET, color_value)


answer_white = 0
answer_black = 0
answer_grey = 0

for tile in tiles:
    if tile.color == "White":
        answer_white += 1
    elif tile.color == "Black":
        answer_black += 1
    elif tile.color == "Grey":
        answer_grey += 1

print(answer_white, answer_black, answer_grey)