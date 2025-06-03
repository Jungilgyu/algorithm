import sys

n = int(input())

answer = -1
for x in range(n//5, -1, -1):
    rest = n - (5 * x)
    if rest % 2 == 0:
        y = rest // 2
        answer = x + y
        break

print(answer)


