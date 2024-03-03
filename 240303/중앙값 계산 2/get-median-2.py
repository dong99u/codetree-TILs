import sys
input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

nums_temp = []

for idx in range(len(nums)):

    nums_temp.append(nums[idx])
    # 숫자가 홀수번째 숫자라면
    if idx % 2 == 0:
        nums_temp.sort()
        print(nums_temp[idx // 2], end = ' ')