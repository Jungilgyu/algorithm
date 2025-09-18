import sys
input = sys.stdin.readline

n, m = map(int, input().split())

area = [list(map(int, input().split())) for _ in range(n)]

di = [0,1,0]
dj = [-1,0,1]

dp = [[0] * m for _ in range(n)]
dp[0][0] = area[0][0]

# 첫줄만 미리
for j in range(1, m):
    dp[0][j] = dp[0][j-1] + area[0][j]

for i in range(1, n):
    # 1. 좌 => 우 검사
    left = [0] * m
    left[0] = dp[i-1][0] + area[i][0]
    for j in range(1, m):
        left[j] = max(left[j-1] + area[i][j], dp[i-1][j] + area[i][j])

    # 2. 우 => 좌 검사
    right = [0] * m
    right[m-1] = dp[i-1][m-1] + area[i][m-1]
    for j in range(m-2, -1, -1):
        right[j] = max(right[j+1] + area[i][j], dp[i-1][j] + area[i][j])

    for j in range(m):
        dp[i][j] = max(left[j], right[j])

print(dp[n-1][m-1])