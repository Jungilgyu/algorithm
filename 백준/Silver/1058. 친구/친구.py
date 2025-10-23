import sys
input = sys.stdin.readline

n = int(input())
arr = [list(input().strip()) for _ in range(n)]

dist  = [[float('inf')] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            dist[i][j] = 0
        elif arr[i][j] == 'Y':
            dist[i][j] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

ans = 0
for i in range(n):
    cnt = 0
    for j in range(n):
        if i != j and dist[i][j] <= 2:
            cnt += 1
    ans = max(ans, cnt)
print(ans)


