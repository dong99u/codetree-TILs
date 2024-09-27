import sys
from collections import defaultdict
input = sys.stdin.readline

n, k = map(int, input().split())

d = defaultdict(int)

for num in list(map(int, input().split())):
    d[num] += 1

answer = 0
for key in d.keys():
    if d[key] >= 1:
        find_num = k - key

        if find_num in d:
            d[find_num] -= 1
            answer += 1


print(answer)