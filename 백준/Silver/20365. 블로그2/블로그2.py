import sys
input = sys.stdin.readline

n = int(input())
target = input().strip()

r = 0
b = 0

# 첫 덩어리
prev = target[0]
if prev == 'R':
    r += 1
else:
    b += 1

for i in range(1, n):
    if target[i] != prev:
        if target[i] == 'R':
            r += 1
        else:
            b += 1

        prev = target[i]

print(min(r, b) + 1)



