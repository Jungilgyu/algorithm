import sys

k = int(input())
n = int(input())
end = list(input())

ladder = [list(input()) for _ in range(n)]

start = sorted(end)

q_line = 0
for i in range(n):
    if ladder[i][0] == '?':
        q_line = i
        break

# 내려가기
def down(start):
    for i in range(q_line):
        for j in range(k-1):
            if ladder[i][j] == "-":
                 start[j], start[j+1] = start[j+1], start[j]
    return start

def up(end):
    for i in range(n-1, q_line, -1):
        for j in range(k-1):
            if ladder[i][j] == "-":
                 end[j], end[j+1] = end[j+1], end[j]
    return end

def check(res_up, res_down, ans):
    for j in range(k-1):
        if ans[j] == "-":
            res_down[j], res_down[j+1] = res_down[j+1], res_down[j]

    if res_up == res_down:
        print(''.join(map(str, ans)))
    else:
        cant_find = 'x' * (k-1)
        print(cant_find)

res_down = down(start)
res_up = up(end)


ans = [''] * (k-1)
idx = 0
while idx < k-1:
    if res_down[idx] != res_up[idx]:
        ans[idx] = '-'
        idx += 1
    if idx >= k-1:
        break
    ans[idx] = '*'
    idx += 1

check(res_down, res_up, ans)

