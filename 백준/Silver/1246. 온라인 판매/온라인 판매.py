import sys
input = sys.stdin.readline

n, m = map(int, input().split())
p = list(int(input()) for _ in range(m))

p.sort()

max_p = 0
total = 0

# 달걀 < 고객
# 달걀 >= 고객
for i in range(m-min(n, m), m):
    temp = p[i] * (m - i)
    if temp > total:
        total = temp
        max_p = p[i]

print(max_p, total)






