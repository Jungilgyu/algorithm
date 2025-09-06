import sys
input = sys.stdin.readline


n = int(input())
checker = [list(map(int, input().split())) for _ in range(n)]

xs = [x for x, _ in checker]
ys = [y for _, y in checker]

ans = [float('inf')] * (n+1)

for cx in xs:
    for cy in ys:
        dist = []
        for x, y in checker:
            distance = abs(cx - x) + abs(cy - y)
            dist.append(distance)

        dist.sort()
        total = 0
        for k in range(1, n+1):
            total += dist[k-1]
            ans[k] = min(ans[k], total)

print(*ans[1:])











