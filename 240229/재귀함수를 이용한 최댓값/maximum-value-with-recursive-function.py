n = int(input())

l = list(map(int, input().split()))

def get_max(max_val, idx, n):
    if idx == n:
        return max_val
    
    if max_val < l[idx]:
        return get_max(l[idx], idx + 1, n)
    else:
        return get_max(max_val, idx + 1, n)

result = get_max(l[0], 0, n)

print(result)