import sys
from collections import Counter

r, c, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(3)]

# for x in a:
#     counter = Counter(t for t in x if t != 0)
#     print(counter.items())

def sort_line(line):
    counter = Counter(x for x in line if x != 0)
    sorted_items = sorted(counter.items(), key=lambda x: (x[1], x[0]))

    result = []
    for num, cnt in sorted_items:
        result.extend([num, cnt])
    return result[:100]

def R_operation(a):
    max_len = 0
    new_a = []
    for row in a:
        new_row = sort_line(row)
        max_len = max(max_len, len(new_row))
        new_a.append(new_row)

    for i in range(len(new_a)):
        new_a[i] += [0] * (max_len - len(new_a[i]))
    return new_a

def C_operation(a):
    transposed = list(map(list, zip(*a)))
    transposed = R_operation(transposed)
    return list(map(list, zip(*transposed)))


time = 0
while time <= 100:
    if r - 1 < len(a) and c - 1 < len(a[0]) and a[r-1][c-1] == k:
        print(time)
        break

    if len(a) >= len(a[0]):
        a = R_operation(a)
    else:
        a = C_operation(a)

    time += 1

else:
    print(-1)

