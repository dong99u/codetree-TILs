# Read 4x4 grid
grid = [list(map(int, input().split())) for _ in range(4)]

# Read direction
dir = input()


# Please write your code here.

def check(arr, dir_num):
    '''
    dir_num == 0: 왼쪽으로 압축
    dir_num == 1: 오른쪽으로 압축
    '''
    result = []
    for num in arr:
        if num != 0:
            result.append(num)

    if dir_num == 0:
        result += [0] * (4 - len(result))
        for i in range(1, 4):
            if result[i - 1] == result[i]:
                result[i - 1] += result[i]
                result[i] = 0
            elif result[i - 1] == 0:
                result[i - 1] = result[i]
                result[i] = 0

        return result

    else:
        result = [0] * (4 - len(result)) + result

        for i in range(2, -1, -1):
            if result[i] == result[i + 1]:
                result[i + 1] += result[i]
                result[i] = 0
            elif result[i + 1] == 0:
                result[i + 1] = result[i]
                result[i] = 0

        return result


if dir == 'L' or dir == 'R':
    for row_idx, row in enumerate(grid):
        if dir == 'L':
            arr = check(row, 0)
            grid[row_idx] = arr
        else:
            arr = check(row, 1)
            grid[row_idx] = arr

if dir == 'U' or dir == 'D':
    for col_idx, col in enumerate(zip(*grid)):
        if dir == 'U':
            arr = check(col, 0)
            for row_idx, num in enumerate(arr):
                grid[row_idx][col_idx] = num
        else:
            arr = check(col, 1)
            for row_idx, num in enumerate(arr):
                grid[row_idx][col_idx] = num

for row in grid:
    print(*row)

