import sys
from collections import deque
input = sys.stdin.readline

k = int(input())
w, h = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(h)]

# 그냥이동
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# 점프이동
ji = [-2, -1, 1, 2, 2, 1, -1, -2]
jj = [1, 2, 2, 1, -1, -2, -2, -1]

visited = [[[False] * w for _ in range(h)] for _ in range(k+1)]
# visited[k][i][j] = 찬스 k개들고  i, j 도달


def bfs():
    q = deque()
    q.append([0, 0, 0, k])
    visited[k][0][0] = True

    while q:
        ci, cj, cnt, chance = q.popleft()

        if ci == h-1 and cj == w-1:
            return cnt

        # 1. 점프이동할지
        if chance > 0:
            for d in range(8):
                ni, nj = ci + ji[d], cj + jj[d]
                if 0 <= ni < h and 0 <= nj < w and area[ni][nj] != 1 and not visited[chance-1][ni][nj]:
                    q.append([ni, nj, cnt+1, chance-1])
                    visited[chance-1][ni][nj] = True

        # 2. 그냥이동할지
        for d in range(4):
            ni , nj = ci + di[d], cj + dj[d]
            if 0 <= ni < h and 0 <= nj < w and area[ni][nj] != 1 and not visited[chance][ni][nj]:
                q.append([ni, nj, cnt+1, chance])
                visited[chance][ni][nj] = True

    return -1

print(bfs())

