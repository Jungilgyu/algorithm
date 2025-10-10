import sys
input = sys.stdin.readline

n = int(input())
p = [int(input()) for _ in range(n)]
p.append(1000001)

p.sort(reverse=True)

ans = 0
for i in range(1, n+1):
    if i % 3 != 0:
        ans += p[i]
print(ans)


