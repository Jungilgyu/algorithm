import sys
input = sys.stdin.readline

MAX_N = 10000
dp = [0] * (MAX_N + 1)
dp[0] = 1

# 딱 한 번만 전체 dp 계산
for num in [1, 2, 3]:
    for i in range(num, MAX_N + 1):
        dp[i] += dp[i - num]

# 이제 입력받고 바로 출력
t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n])
