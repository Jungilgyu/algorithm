

match = {
        0: 6, 1: 2, 2: 5, 3: 5, 4: 4,
        5: 5, 6: 6, 7: 3, 8: 7, 9: 6
    }

# 1. dp[i] = i개로 만들 수 있는 가장 작은 수
dp = [""] * 101
# dp = [0, 0, 1, 7, 4, 2]
dp[2] = "1"
dp[3] = "7"
dp[4] = "4"
dp[5] = "2"
dp[6] = "6"
dp[7] = "8"

for i in range(8, 101):
    dp[i] = "9" * 100   
    for d, cost in match.items():
        if i - cost >= 2 and dp[i - cost] != "":
            cand = dp[i - cost] + str(d)
            # 숫자 비교: 자리 수 → 사전순
            if len(cand) < len(dp[i]) or (len(cand) == len(dp[i]) and cand < dp[i]):
                dp[i] = cand

t = int(input())
for _ in range(t):
    n = int(input())
    max_val = 0
    if n % 2 == 0: # 짝수
        max_val = '1' * (n//2)
    else:
        if n == 3:
            max_val = '7'
        else:
            max_val = '7' + '1' * ((n-3) // 2)

    print(dp[n], max_val)

