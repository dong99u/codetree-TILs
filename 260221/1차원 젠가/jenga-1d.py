n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

# Please write your code here.

temp = []

for i in range(len(blocks)):
    if s1 - 1 <= i <= e1 - 1:
        continue

    temp.append(blocks[i])

blocks = temp
temp = []

for i in range(len(blocks)):
    if s2 - 1 <= i <= e2 - 1:
        continue
    temp.append(blocks[i])

blocks = temp

print(len(blocks))

for num in blocks:
    print(num)