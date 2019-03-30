from math import sqrt
num_trees = int(input())
length, width = [int(n) for n in input().split()]

pos = []
for _ in range(num_trees):
    pos.append(int(input()))
pos.sort()

split_dist = length / (num_trees / 2 - 1)

left, right = [[], []]
for i in range(0, int(num_trees / 2)):
    left.append(i * split_dist)
    right.append(i * split_dist)

total_dist = 0

for i in range(0, len(pos), 2):
    first = abs(left[0] - pos[i])
    second = abs(left[0] - pos[i + 1])

    if first < second:
        # first is shorter
        total_dist += first
        left.pop(0)

        # work on second now
        total_dist += sqrt((pos[i+1] - right[0]) ** 2 + width ** 2)
        right.pop(0)

    else:
        # second is shorter
        total_dist += second
        left.pop(0)

        # left side now
        total_dist += sqrt((pos[i] - right[0]) ** 2 + width ** 2)
        right.pop(0)


print(total_dist)

