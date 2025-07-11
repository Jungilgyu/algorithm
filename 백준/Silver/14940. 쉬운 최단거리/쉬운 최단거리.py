import sys
from collections import deque
# sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

res = [[0] * m for _ in range(n)]

def bfs(sx, sy):
    q = deque()
    q.append([sx, sy])
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + di[k], y + dj[k]
            if 0 <= nx < n and 0 <= ny < m and res[nx][ny] == 0 and area[nx][ny] == 1:
                res[nx][ny] = res[x][y] + 1
                q.append([nx, ny])


for i in range(n):
    for j in range(m):
        if area[i][j] == 2:
            bfs(i, j)


for i in range(n):
    for j in range(m):
        if area[i][j] == 1 and res[i][j] == 0:
            res[i][j] = -1

for x in res:
    print(*x)

