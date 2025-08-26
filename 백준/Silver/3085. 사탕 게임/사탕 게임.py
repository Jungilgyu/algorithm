import sys

n = int(input())
area = [list(input()) for _ in range(n)]

def check(i, j, ni, nj):
    max_len = 0
    # 가로 검사1
    cnt = 1
    for col in range(1, n):
        if area[i][col] == area[i][col-1]:
            cnt += 1
        else:
            max_len = max(max_len, cnt)
            cnt = 1 # 새걸로 교체
    max_len = max(max_len, cnt)

    # 가로검사 2
    cnt = 1
    for col in range(1, n):
        if area[ni][col] == area[ni][col - 1]:
            cnt += 1
        else:
            max_len = max(max_len, cnt)
            cnt = 1  # 새걸로 교체
    max_len = max(max_len, cnt)

    # 세로 검사1
    cnt = 1
    for row in range(1, n):
        if area[row][j] == area[row-1][j]:
            cnt += 1
        else:
            max_len = max(max_len, cnt)
            cnt = 1
    max_len = max(max_len, cnt)

    # 세로 검사2
    cnt = 1
    for row in range(1, n):
        if area[row][nj] == area[row - 1][nj]:
            cnt += 1
        else:
            max_len = max(max_len, cnt)
            cnt = 1
    max_len = max(max_len, cnt)


    return max_len

di = [0, 1] # 오른쪽, 아래
dj = [1, 0]

ans = 0
# 1. 초기 최장값 찾기
for i in range(n): # 가로줄 하나씩
    cnt = 1
    for j in range(1, n):
        if area[i][j] == area[i][j-1]:
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 1
    ans = max(ans, cnt)

for j in range(n):
    cnt = 1
    for i in range(1, n):
        if area[i][j] == area[i-1][j]:
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 1
    ans = max(ans, cnt)

for i in range(n):
    for j in range(n):
        for k in range(2):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < n and 0 <= nj < n:
                area[i][j], area[ni][nj] = area[ni][nj], area[i][j]
                ans = max(ans, check(i, j, ni, nj))
                area[i][j], area[ni][nj] = area[ni][nj], area[i][j]

print(ans)
