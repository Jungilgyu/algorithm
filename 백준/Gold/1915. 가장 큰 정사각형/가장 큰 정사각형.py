import sys

n, m = map(int, input().split())
area = [list(map(int, input())) for _ in range(n)]

# 변하는 값은 area 내부의 사각형의 가로, 세로 => 2개 변함
# 2차원 dp

dp = [[0] * m for _ in range(n)]
# dp[i][j]는 (i,j)를 오른쪽 아래 꼭지점으로 가지는 정사각형의 한변의 길이
res = 0

for i in range(n):
    for j in range(m):
        if area[i][j] == 1:
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

            res = max(res, dp[i][j])

print(res**2)