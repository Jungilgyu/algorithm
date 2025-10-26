import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
room = [list(input().strip()) for _ in range(n)]

visited = [[False] * m for _ in range(n)]
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
ans = 0

def dfs(i, j):
    global ans

    if room[i][j] == 'P':
        ans += 1

    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and room[ni][nj] != 'X':
            visited[ni][nj] = True
            dfs(ni, nj)

si, sj = -1 ,-1
for i in range(n):
    for j in range(m):
        if room[i][j] == 'I':
            si, sj = i, j
            dfs(si, sj)
            break
if ans == 0:
    print("TT")
else:
    print(ans)



