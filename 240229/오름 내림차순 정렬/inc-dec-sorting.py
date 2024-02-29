n = int(input())

l = list(map(int, input().split()))
print(*sorted(l))
print(*list(reversed(sorted(l))))