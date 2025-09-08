import sys
input = sys.stdin.readline

n = int(input())
lst = [int(input()) for _ in range(n)]
# 양수, 0, 음수 로 분리
plus = []
zero = []
minus = []
for num in lst:
    if num > 0:
        plus.append(num)
    elif num < 0:
        minus.append(num)
    else:
        zero.append(num)

ans = 0
plus.sort(reverse=True)
minus.sort()

# plus부터
i = 0
while i < len(plus) -1:
    # 곱한게 더 크면
    if plus[i] * plus[i+1] > plus[i] + plus[i+1]:
        ans += plus[i] * plus[i+1]
        i += 2
    else: # 곱한게 더작음 1,1 같은 경우
        ans += plus[i]
        i += 1

if i < len(plus):
    ans += plus[i]

# minus
j = 0
while j < len(minus) -1:
    ans += minus[j] * minus[j+1]
    j += 2

# 꽁다리 남음
if j < len(minus):
    if len(zero) == 0:
        ans += minus[j]


print(ans)

