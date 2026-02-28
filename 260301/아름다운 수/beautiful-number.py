import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())

# Please write your code here.
def backtrack(selected, depth):
    if depth == n:
        if check(selected): return 1
        return 0

    count = 0
    for i in range(1, 4 + 1):
        count += backtrack(selected + [i], depth + 1)

    return count

def check(nums):
    left, right = 0, 0
    while left <= right and right < n:
        valid_count = nums[left]
        while right < n and nums[left] == nums[right]:
            right += 1
        if not (right - left) % valid_count == 0:
            return False
        left = right

    return True

answer = backtrack([], 0)
print(answer)