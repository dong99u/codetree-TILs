n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]


def rotate():
    global grid
    temp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp[j][n - 1 - i] = grid[i][j]
    grid = temp


def drop():
    for j in range(n):
        nums = [grid[i][j] for i in range(n) if grid[i][j] != 0]
        nums = [0] * (n - len(nums)) + nums
        for i in range(n):
            grid[i][j] = nums[i]


def boom():
    """연쇄 폭발까지 처리. 터진 게 있으면 True 반환."""
    changed = False
    for j in range(n):
        nums = [grid[i][j] for i in range(n) if grid[i][j] != 0]

        if not nums:
            continue

        # 연쇄 폭발: 더 이상 터질 게 없을 때까지 반복
        while True:
            result = []
            did_explode = False
            i = 0
            while i < len(nums):
                # 연속 그룹의 끝 찾기
                end = i + 1
                while end < len(nums) and nums[end] == nums[i]:
                    end += 1

                if end - i >= m:
                    did_explode = True  # 터뜨림 (result에 안 넣음)
                else:
                    result.extend(nums[i:end])  # 안 터지면 유지

                i = end

            nums = result
            if not did_explode:
                break

        if len(nums) != sum(1 for i in range(n) if grid[i][j] != 0):
            changed = True

        nums = [0] * (n - len(nums)) + nums
        for i in range(n):
            grid[i][j] = nums[i]

    return changed


# 처음에 한 번 터뜨리기
drop()
boom()

# k번: 회전 → 내리기 → 터뜨리기
for _ in range(k):
    rotate()
    drop()
    boom()

answer = sum(1 for i in range(n) for j in range(n) if grid[i][j] != 0)
print(answer)