n = int(input())

# Please write your code here.
visited = [False] * (n + 1)
selected = []
def backtrack(idx):
    if idx == n:
        print(*selected)
        return

    for curr_num in range(n, 0, -1):
        if not visited[curr_num]:
            selected.append(curr_num)
            visited[curr_num] = True
            backtrack(idx + 1)
            visited[curr_num] = False
            selected.pop()

backtrack(0)