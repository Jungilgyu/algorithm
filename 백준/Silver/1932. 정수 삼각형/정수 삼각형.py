import sys

n = int(input())
tri = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]
dp[0][0] = tri[0][0]
for i in range(1, n):
    for j in range(len(tri[i])):
        left = j-1
        right = j

        if 0 <= left < n:
            dp[i][j] = max(dp[i][j], dp[i-1][left] + tri[i][j])

        if 0 <= right < n:
            dp[i][j] = max(dp[i][j], dp[i-1][right] + tri[i][j])

print(max(max(row) for row in dp))

