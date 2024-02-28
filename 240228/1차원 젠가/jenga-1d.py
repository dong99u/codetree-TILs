def cut_blocks(start_index, end_index):
    global blocks

    temp = []

    for i in range(len(blocks)):
        if start_index - 1 <= i <= end_index - 1:
            continue

        temp.append(blocks[i])

    blocks = temp

# 블럭의 개수
n = int(input())

# 블럭의 정보
blocks = [
    int(input())
    for _ in range(n)
]

# 뺄 블럭의 index
for _ in range(2):
    s, e = tuple(map(int, input().split()))

    cut_blocks(s, e)

print(len(blocks))

for elem in blocks:
    print(elem)