import sys
input = sys.stdin.readline

n, m1 = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

m2, k = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(m2)]


ans = [[0] * k for _ in range(n)]

for i in range(n):
    for j in range(k):
        for t in range(m1):
            ans[i][j] += a[i][t] * b[t][j]

for row in ans:
    print(*row)