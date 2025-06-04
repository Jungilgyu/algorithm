import sys

n = int(sys.stdin.readline())
rope = [int(sys.stdin.readline()) for _ in range(n)]

rope.sort()

max_v = 0
for i in range(n):
    max_v = max(max_v, rope[i] * (n - i))

print(max_v)
