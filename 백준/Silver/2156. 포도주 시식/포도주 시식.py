import sys
input = sys.stdin.readline

n = int(input())
cups = [int(input()) for _ in range(n)]
if n == 1:
    print(cups[0])
elif n == 2:
    print(sum(cups))
else:
    dp = [0] * n
    dp[0] = cups[0]
    dp[1] = dp[0] + cups[1]
    dp[2] = max(dp[1], dp[0] + cups[2], cups[1] + cups[2])
    for i in range(3, n):
        dp[i] = max(dp[i-1], dp[i-2] + cups[i], dp[i-3] + cups[i-1] + cups[i])

    print(dp[n-1])

