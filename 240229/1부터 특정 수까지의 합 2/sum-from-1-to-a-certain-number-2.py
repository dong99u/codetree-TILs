def get_sum(n):
    if n == 1:
        return 1

    return get_sum(n - 1) + n

N = int(input())
print(get_sum(N))