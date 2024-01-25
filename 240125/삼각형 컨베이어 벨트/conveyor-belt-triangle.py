n, t = map(int, input().split())

left = list(map(int, input().split()))
right = list(map(int, input().split()))
bottom = list(map(int, input().split()))

for _ in range(t):
    left_to_right_temp = left[-1]
    right_to_bottom_temp = right[-1]
    bottom_to_left_temp = bottom[-1]

    # 왼쪽 리스트를 한칸씩 옮김
    for i in range(n - 1, 0, -1):
        left[i] = left[i - 1]
    left[0] = bottom_to_left_temp

    for i in range(n - 1, 0, -1):
        right[i] = right[i - 1]
    right[0] = left_to_right_temp

    for i in range(n - 1, 0, -1):
        bottom[i] = bottom[i - 1]
    bottom[0] = right_to_bottom_temp

print(*left)
print(*right)
print(*bottom)