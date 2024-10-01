from collections import defaultdict

word = input()

d = defaultdict(int)
for w in word:
    d[w] += 1

answer = None
for key, value in d.items():

    if value == 1:
        answer = key
        break

print(answer)