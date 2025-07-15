import sys
from collections import deque

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
arr.append([-1] * m)
# for x in arr:
#     print(x)
# 이동방향
di = [1, 1, 1]
dj = [-1, 0, 1]

def sol(si, sj):
    q = deque()
    q.append([si, sj, arr[si][sj], -1])
    res = []
    while q:
        x, y, c, prev_d = q.popleft()

        # if arr[x][y] == -1:
        #     return c

        for k in range(3):
            nx, ny = x + di[k], y + dj[k]
            if 0 <= nx < n and 0 <= ny < m and k != prev_d:
                q.append([nx, ny, c+arr[nx][ny], k])
            elif nx == n:
                res.append(c)

    return res

ans = []
for j in range(m):
    temp = sol(0, j)
    ans.extend(temp)
print(min(ans))