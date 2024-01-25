n = int(input()) # 2 <= n <= 100

jenga = [
    int(input()) for _ in range(n)
]

s1, e1 = map(int, input().split())
first_extract_cnt = e1 - s1 + 1
s2, e2 = map(int, input().split())

temp_jenga = []

# 첫 빼기
for jenga_idx in range(n):
    if jenga_idx in list(range(s1 - 1, e1)):
        continue
    
    temp_jenga.append(jenga[jenga_idx])

jenga = temp_jenga[:]
temp_jenga = []

# 두번째 빼기
for jenga_idx in range(n - first_extract_cnt):
    if jenga_idx in list(range(s2 - 1, e2)):
        continue
    
    temp_jenga.append(jenga[jenga_idx])

jenga = temp_jenga[:]

print(len(jenga))
for i in range(len(jenga)):
    print(jenga[i])