import sys
import math
input = sys.stdin.readline

n, m = map(int, input().split())
area = [list(map(int, input().strip())) for _ in range(n)]

ans = -1

for i in range(n):
    for j in range(m):
        for dr in range(-n, n):
            for dc in range(-m, m):
                if dr == 0 and dc == 0:
                    continue

                num = 0
                r, c = i, j
                while 0 <= r < n and 0 <= c < m:
                    num = num * 10 + area[r][c]
                    if int(math.isqrt(num)) ** 2 == num:
                        ans = max(ans, num)
                    r += dr
                    c += dc

print(ans)
