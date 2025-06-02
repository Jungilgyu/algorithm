import sys

n = int(input())

prefer = [[] for _ in range(n**2+1)]
students = []
for _ in range(n**2):
    lst = list(map(int, input().split()))
    students.append(lst[0])
    prefer[lst[0]].extend(lst[1:])

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

area = [[0] * n for _ in range(n)]
satis = [0] * (n**2 + 1)

def rule(s):
    res1 = [] # 후보
    max_cnt1 = 0
    for i in range(n):
        for j in range(n):
            if area[i][j] == 0:
                temp = 0
                for k in range(4):
                    ni, nj = i + di[k], j + dj[k]
                    if 0 <= ni < n and 0 <= nj < n and area[ni][nj] in prefer[s]:
                        temp += 1
                if temp > max_cnt1:
                    max_cnt1 = temp
                    res1 = [[i, j]]
                elif temp == max_cnt1:
                    res1.append([i, j])

    # 2.
    res2 = []
    max_cnt2 = 0
    for x, y in res1:
        temp = 0
        for k in range(4):
            nx, ny = x + di[k], y + dj[k]
            if 0 <= nx < n and 0 <= ny < n and area[nx][ny] == 0:
                temp += 1
        if temp > max_cnt2:
            max_cnt2 = temp
            res2 = [[x, y]]
        elif temp == max_cnt2:
            res2.append([x, y])

    # 3.
    res3 = sorted(res2, key=lambda x: (x[0], x[1]))

    return res3[0]


for s in students:
    row, col = rule(s)
    area[row][col] = s

ans = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        temp = area[i][j]
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < n and 0 <= nj < n and area[ni][nj] in prefer[temp]:
                cnt += 1
        if cnt != 0:
            ans += 10 ** (cnt-1)

print(ans)