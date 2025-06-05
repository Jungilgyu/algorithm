import sys
from collections import deque

di = [0, 1, 0, -1, -1, -1, 1, 1]
dj = [1, 0, -1, 0, -1, 1, -1, 1]

def bfs(i, j):
    q = deque()
    q.append([i, j])
    visited[i][j] = True

    while q:
        x, y, = q.popleft()

        for k in range(8):
            nx, ny = x + di[k], y + dj[k]
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and area[nx][ny] == 1:
                q.append([nx, ny])
                visited[nx][ny] = True
    return

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    area = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if area[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                cnt += 1

    print(cnt)



