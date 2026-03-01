from collections import defaultdict

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
MAX_COUNT = len(edges)
d = defaultdict(list)

for col, row in edges:
    d[row].append((col, row))

def simulate(sc, d):
    cr, cc = 1, sc

    while cr <= 15:
        for col, row in d.get(cr, []):
            if cc == col:
                cc += 1
            elif cc == col + 1:
                cc -= 1
        cr += 1

    return cc

def simulate_all(d):
    result = [0] * (n + 1)
    for i in range(1, n + 1):
        idx = simulate(i, d)
        result[idx] = i

    return result

def backtrack(idx, count, d, max_result):
    if idx == m:
        if simulate_all(d) == first_result:
            return count
        else:
            return MAX_COUNT
    if count >= max_result:
        return MAX_COUNT
    result = simulate_all(d)
    if result == first_result:
        return count

    result = MAX_COUNT
    c, r = edges[idx]
    d[r].append((c, r))
    result = min(result, backtrack(idx + 1, count + 1, d, result))
    d[r].pop()
    result = min(result, backtrack(idx + 1, count, d, result))

    return result

first_result = simulate_all(d)
backtrack_d = defaultdict(list)
answer = backtrack(0, 0, backtrack_d, MAX_COUNT)
print(answer)
