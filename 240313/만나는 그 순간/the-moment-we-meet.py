n, m = tuple(map(int, input().split()))

A = [0]
B = [0]

curr_x = 0
for _ in range(n):
    d, t = input().split()
    t = int(t)

    if d == 'L':

        for _ in range(t):
            curr_x -= 1
            A.append(curr_x)
    
    if d == 'R':

        for _ in range(t):
            curr_x += 1
            A.append(curr_x)
curr_x = 0
for _ in range(m):
    d, t = input().split()
    t = int(t)

    if d == 'L':

        for _ in range(t):
            curr_x -= 1
            B.append(curr_x)

    if d == 'R':

        for _ in range(t):
            curr_x += 1
            B.append(curr_x)
is_meet = False
for i in range(1, len(A)):

    if A[i] == B[i]:
        print(i)
        is_meet = True
        break

if not is_meet:
    print(-1)