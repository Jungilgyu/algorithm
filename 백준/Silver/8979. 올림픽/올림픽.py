import sys
input = sys.stdin.readline
n, k = map(int, input().split())
ranking = [list(map(int, input().split())) for _ in range(n)]

res = sorted(ranking, key=lambda x: (x[1], x[2], x[3]), reverse=True)
ans = 0
g, s, b = 0, 0, 0
for x in res:
    if x[0] == k:
        break
    else:
        # 메달수가 다 같음
        if g == x[1] and s == x[2] and b == x[3]:
            continue
        else:
            g, s, b = x[1], x[2], x[3]
            ans += 1


print(ans)

