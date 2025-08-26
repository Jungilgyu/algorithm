import sys

n = int(input())
nums = list(map(int, input().split()))

dp = [[0] * 21 for _ in range(n-1)]
dp[0][nums[0]] = 1

for i in range(n-2):
    for v in range(21):
        if dp[i][v]: # dp[1][10] / dp[1][6]
            plus = v + nums[i+1]
            minus = v - nums[i+1]
            if 0 <= plus <= 20:
                dp[i+1][plus] += dp[i][v]
            if 0 <= minus <= 20:
                dp[i+1][minus] += dp[i][v]

print(dp[n-2][nums[-1]])




