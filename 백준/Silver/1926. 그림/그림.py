import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

area = [list(map(int, input().split())) for _ in range(n)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(si, sj):
    global max_size
    q = deque()
    q.append((si, sj))
    visited[si][sj] = True

    size = 1
    while q:
        ci, cj = q.popleft()

        for k in range(4):
            ni, nj = ci + di[k], cj + dj[k]
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and area[ni][nj] == 1:
                q.append((ni, nj))
                visited[ni][nj] = True
                size += 1

    max_size = max(max_size, size)


visited = [[False] * m for _ in range(n)]

cnt = 0
max_size = 0
for i in range(n):
    for j in range(m):
        if area[i][j] == 1 and not visited[i][j]:
            bfs(i, j)
            cnt += 1


print(cnt)
print(max_size)