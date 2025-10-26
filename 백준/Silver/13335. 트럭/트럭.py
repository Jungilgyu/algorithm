import sys
from collections import deque
input = sys.stdin.readline

n, w, L = map(int, input().split())
truck = list(map(int, input().split()))

b = deque([0] * w)

time = 0
weight = 0
for t in truck:
    while True:
        time += 1
        left = b.popleft()
        weight -= left

        if weight + t <= L:
            b.append(t)
            weight += t
            break
        else:
            b.append(0)

while b:
    b.popleft()
    time += 1
print(time)




