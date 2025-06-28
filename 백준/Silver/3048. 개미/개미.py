import sys


n1_cnt, n2_cnt = map(int, input().split())
n1 = list(input())
n2 = list(input())
t = int(input())

# 좌 => 우
for i in range(n1_cnt):
    n1[i] = [n1[i], 1]

# 우 => 좌
for j in range(n2_cnt):
    n2[j] = [n2[j], -1]

start = []

for i in range(n1_cnt-1, -1, -1):
    start.append(n1[i])

for j in range(n2_cnt):
    start.append(n2[j])


while True:
    if t == 0:
        break

    change = []
    for i in range(n1_cnt + n2_cnt - 1):
        if (start[i][1] == 1 and start[i+1][1] == -1):
            change.append(i)

    for x in change:
        start[x], start[x+1] = start[x+1], start[x]

    t -= 1

ans = ""
for i in range(n1_cnt + n2_cnt):
    ans += start[i][0]

print(ans)
