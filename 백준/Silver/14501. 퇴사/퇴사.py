import sys

n = int(input())
tp = [list(map(int, input().split())) for _ in range(n)]

dp = [0] * (n+1)
# dp[n] = n일차에 얻을 수 있는 최대 이익

ans = 0
for i in range(n):
    t, p = tp[i]
    dp[i] = max(dp[i], dp[i-1])
    if i + t <= n:
        dp[i+t] = max((dp[i]+p), dp[i+t])

print(max(dp))
#
# 1일에
# t=3, p=10
# dp = [0, 0, 0, 10]
#
# 2일
# t=5, p=20
#
# dp = [0, 0, 0, 0, 0, 0, 20]
# dp[7] = max((dp[1] + tp[2]), dp[6])
