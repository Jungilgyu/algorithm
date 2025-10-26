import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
room = [list(input().strip()) for _ in range(n)]

visited = [[False] * m for _ in range(n)]
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


def bfs(i, j):
    q = deque()
    q.append([i, j])
    visited[i][j] = True

    res = 0
    while q:
        ci, cj = q.popleft()

        if room[ci][cj] == 'P':
            res += 1

        for k in range(4):
            ni, nj = ci + di[k], cj + dj[k]
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and room[ni][nj] != 'X':
                q.append([ni, nj])
                visited[ni][nj] = True

    return res


si, sj = -1 ,-1
ans = 0
for i in range(n):
    for j in range(m):
        if room[i][j] == 'I':
            si, sj = i, j
            ans = bfs(si, sj)
            break

if ans == 0:
    print("TT")
else:
    print(ans)



