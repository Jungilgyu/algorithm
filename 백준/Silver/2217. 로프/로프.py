import sys


n = int(input())
rope = []
for _ in range(n):
    max_w = int(input())
    rope.append(max_w)


rope.sort()

max_v = 0
for i in range(n):
    max_v = max(max_v, rope[i] * (n-i))

print(max_v)
