import sys

n = int(input())
exp = [int(input()) for _ in range(n)]
# print(exp)

ans = 0
for i in range(n-2, -1, -1):
    if exp[i] >= exp[i+1]:
        score = exp[i+1] - 1
        ans += (exp[i] - score)
        exp[i] = score


print(ans)