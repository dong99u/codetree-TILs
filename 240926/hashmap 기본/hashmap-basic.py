import sys
input = sys.stdin.readline

n = int(input())

hash_map = dict()

for _ in range(n):

    user_input = input().split()

    if user_input[0] == 'add':
        hash_map[user_input[1]] = user_input[2]
    elif user_input[0] == 'remove':
        hash_map.pop(user_input[1])
    elif user_input[0] == 'find':
        if user_input[1] in hash_map:
            print(hash_map[user_input[1]])
        else:
            print(None)