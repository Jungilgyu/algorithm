import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())

f = set()
for _ in range(k):
    r, c = map(int, input().split())
    f.add((r-1, c-1))

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

visited = set()

def bfs(si, sj):
    q = deque()
    q.append((si ,sj))
    visited.add((si, sj))

    size = 1
    while q:
        ci, cj = q.popleft()

        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]
            if 0 <= ni < n and 0 <= nj < m and (ni, nj) in f and (ni, nj) not in visited:
                q.append((ni, nj))
                visited.add((ni, nj))
                size += 1

    return size

ans = 0
for i in range(n):
    for j in range(m):
        if (i, j) in f and (i, j) not in visited:
            ans = max(ans, bfs(i, j))
            
print(ans)



