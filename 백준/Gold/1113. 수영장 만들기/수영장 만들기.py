import sys
from collections import deque

n, m = map(int, input().split())
area = [list(map(int, input())) for _ in range(n)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(i, j, h):
    q = deque()
    q.append([i, j])
    visited[i][j] = True

    conn = [[i, j]]
    adj_outline = False
    while q:
        x, y = q.popleft()

        for k in range(4):
            nx, ny = x + di[k], y + dj[k]
            if 0 <= nx < n and 0 <= ny < m :
                if not visited[nx][ny] and area[nx][ny] < h:
                    q.append([nx, ny])
                    visited[nx][ny] = True
                    conn.append([nx, ny])
            else:
                adj_outline = True

    if adj_outline:
        return -1

    res = 0
    for x, y in conn:
        res += h - area[x][y]
        area[x][y] = h

    return res


ans = 0
for h in range(2, 10):
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if area[i][j] < h and not visited[i][j]:
                # 붙어있는 칸중에 높이가 같은 애들을 다 구해
                temp = bfs(i, j, h)

                if temp == -1:
                    continue
                else:
                    ans += temp


print(ans)