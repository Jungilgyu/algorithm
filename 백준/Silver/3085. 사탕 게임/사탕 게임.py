import sys
input = sys.stdin.readline

n = int(input())
area = [list(input()) for _ in range(n)]

def check():
    max_len = 0
    # 가로 검사
    for i in range(n): # 가로줄 하나씩
        cnt = 1
        for j in range(1, n):
            if area[i][j] == area[i][j-1]:
                cnt += 1
            else:
                max_len = max(max_len, cnt)
                cnt = 1 # 새걸로 교체
        max_len = max(max_len, cnt)

    # 세로 검사
    for j in range(n):
        cnt = 1
        for i in range(1, n):
            if area[i][j] == area[i-1][j]:
                cnt += 1
            else:
                max_len = max(max_len, cnt)
                cnt = 1
        max_len = max(max_len, cnt)

    return max_len

di = [0, 1] # 오른쪽, 아래
dj = [1, 0]

ans = 0
for i in range(n):
    for j in range(n):
        for k in range(2):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < n and 0 <= nj < n:
                area[i][j], area[ni][nj] = area[ni][nj], area[i][j]
                ans = max(ans, check())
                area[i][j], area[ni][nj] = area[ni][nj], area[i][j]

print(ans)
