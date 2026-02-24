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
        # 0이 아닌 숫자만 추출
        nums = [grid[i][j] for i in range(n) if grid[i][j] != 0]
        # 위를 0으로 패딩
        nums = [0] * (n - len(nums)) + nums
        for i in range(n):
            grid[i][j] = nums[i]


def boom():
    """0을 제거한 뒤 연속 그룹만 판별. 터진 게 있으면 True 반환."""
    changed = False
    for j in range(n):
        # 0이 아닌 숫자만 추출 (drop 후이므로 이미 아래로 몰려있음)
        nums = [grid[i][j] for i in range(n) if grid[i][j] != 0]

        if not nums:
            continue

        # 연속 그룹 판별 후 m 미만만 남기기
        result = []
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                if count < m:
                    result.extend([nums[i - 1]] * count)
                count = 1

        # 마지막 그룹 처리
        if count < m:
            result.extend([nums[-1]] * count)

        # 변화가 있었는지 확인
        if len(result) != len(nums):
            changed = True

        # 위를 0으로 패딩 후 반영
        result = [0] * (n - len(result)) + result
        for i in range(n):
            grid[i][j] = result[i]

    return changed


# k번 반복: 터뜨리기 → 내리기 → 회전 → 내리기
for _ in range(k):
    drop()
    boom()
    drop()
    rotate()

# 터질 게 없을 때까지 반복: 터뜨리기 → 내리기 → 회전 → 내리기
drop()
while boom():
    drop()
    rotate()
    drop()

# 남은 숫자 개수 세기
answer = sum(1 for i in range(n) for j in range(n) if grid[i][j] != 0)
print(answer)