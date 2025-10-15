import sys
input = sys.stdin.readline

n = int(input())

t = [int(input()) for _ in range(n)]
t.sort(reverse=True)

ans = 0
for i in range(n):
    tip = t[i] - i
    if tip > 0:
        ans += tip

print(ans)
