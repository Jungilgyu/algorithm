import sys

n = int(input())

# dp => 변하는 값 생각
# idx, 각 자리별 값
dp = [[0] * (10) for _ in range(n+1)]

# dp[i][j] => i번째 값이 j인 경우의 계단수 개수
for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        if j > 0:
            dp[i][j] += dp[i-1][j-1]
        if j < 9:
            dp[i][j] += dp[i-1][j+1]

        dp[i][j] %= 1000000000

# for x in dp:
#     print(x)
print(sum(dp[n]) % 1000000000)
