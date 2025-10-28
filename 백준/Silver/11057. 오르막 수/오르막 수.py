import sys
input = sys.stdin.readline

n = int(input())


dp = [[0] * (n+1) for _ in range(10)]

for i in range(10): # 자리수별 값 
    for j in range(n+1): # 자리수
        if i == 0 or j == 0:
            dp[i][j] = 1

        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(dp[9][n] % 10007)
