import sys

n = int(input())
v = list(map(int, input().split()))

s = 0
e = n-1
min_d = float('inf')
ans_s, ans_e = s, e
while s < e:
    temp = v[s] + v[e]
    if temp < 0:
        if abs(temp) < abs(min_d):
            min_d = abs(temp)
            ans_s, ans_e = s, e
        s += 1
    elif temp > 0:
        if abs(temp) < abs(min_d):
            min_d = abs(temp)
            ans_s, ans_e = s, e
        e -= 1
    elif temp == 0:
        ans_s, ans_e = s, e
        break

ans = [v[ans_s], v[ans_e]]
ans.sort()

print(*ans)

