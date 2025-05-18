import sys

n = int(input())
schedule = [list(map(int, input().split())) for _ in range(n)]

max_day = 0
for s, e in schedule:
    max_day = max(e, max_day)

cal = [0] * (max_day+1)

for s, e in schedule:
    for i in range(s, e+1):
        cal[i] += 1

height = 0
width = 0
ans = 0
for num in cal:
    if num == 0:
        # print(height, width)
        ans += height * width
        height, width = 0, 0
    else:
        width += 1
        height = max(height, num)
ans += height * width
print(ans)
