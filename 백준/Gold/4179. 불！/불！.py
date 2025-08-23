import sys
from collections import deque

r, c = map(int, input().split())
area = [input() for _ in range(r)]
# for x in area:
#     print(x)

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def spread(f):
    while f:
        i, j = f.popleft()
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < r and 0 <= nj < c and fire[ni][nj] == -1 and area[ni][nj] != '#':
                fire[ni][nj] = fire[i][j] + 1
                f.append([ni, nj])


# 지훈 이동후 불확산은 가능할듯?
def sol(ji, jj):
    q = deque()
    q.append([ji, jj, 0])
    visited = [[False] * c for _ in range(r)]
    visited[ji][jj] = True

    while q:
        i, j, cnt = q.popleft()

        if i >= r or i < 0 or j >= c or j < 0: # 범위 밖이면 탈출 성공
            return cnt

        # 다음좌표를 선택할 떄 둘중하나여야함
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            # 1. 범위 밖으로 탈출
            if ni >= r or ni < 0 or nj >= c or nj < 0:
                return cnt + 1

            if not visited[ni][nj] and area[ni][nj] != '#' and (fire[ni][nj] == -1 or cnt + 1< fire[ni][nj]):
                q.append([ni, nj, cnt + 1])
                visited[ni][nj] = True

    return "IMPOSSIBLE"

# 불의 좌표 모두 찾기
fire = [[-1] * c for _ in range(r)]
f = deque()
for i in range(r):
    for j in range(c):
        if area[i][j] == 'F':
            fire[i][j] = 0
            f.append([i, j])

# 지훈이의 시작 좌표
ji, jj = -1, -1
for i in range(r):
    for j in range(c):
        if area[i][j] == "J":
            ji, jj = i, j
spread(f)


print(sol(ji, jj))


