import sys
input = sys.stdin.readline

n = int(input())

sequence = [
    [num, idx + 1] for idx, num in enumerate(list(map(int, input().split())))
]


sequence.sort(key=lambda x: x[0])

for idx, seq in enumerate(sequence):
    seq.append(idx + 1)

sequence.sort(key=lambda x: x[1])

for seq in sequence:
    print(seq[2], end = " ")