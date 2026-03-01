n, m, c = map(int, input().split())
weights = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def backtrack(idx, profit, sum_val, elems):
    if idx == m:
        return profit

    result = 0
    if sum_val + elems[idx] <= c:
        result = max(result, backtrack(idx + 1, profit + elems[idx] ** 2, sum_val + elems[idx], elems))
    result = max(result, backtrack(idx + 1, profit, sum_val, elems))

    return result

def duplicated(r1, c1, r2, c2):
    return r1 == r2 and not (c1 + m <= c2 or c2 + m <= c1)

profits = []
for i in range(n):
    for j in range(n - m + 1):
        elems = weights[i][j:j + m]
        if sum(elems) > c:
            p = backtrack(0, 0, 0, elems)
        else:
            p = sum(x ** 2 for x in elems)
        profits.append((i, j, p))

answer = 0
for a in range(len(profits)):
    for b in range(a + 1, len(profits)):
        r1, c1, p1 = profits[a]
        r2, c2, p2 = profits[b]

        if duplicated(r1, c1, r2, c2):
            continue

        answer = max(answer, p1 + p2)

print(answer)