import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[[float('inf')] * 3 for _ in range(m)] for _ in range(n)]


for j in range(m):
    for d in range(3):
        dp[0][j][d] = arr[0][j]

for i in range(1, n):
    for j in range(m):
        for d in range(3):
            nj = j + (d - 1)
            if 0 <= nj < m:
                for prev_d in range(3):
                    if prev_d != d:
                        dp[i][j][d] = min(dp[i][j][d], dp[i-1][nj][prev_d] + arr[i][j])

ans = float('inf')
for j in range(m):
    for d in range(3):
        ans = min(ans, dp[n-1][j][d])

print(ans)