import sys
from collections import deque
n, q = map(int, input().split())

area = [list(map(int, input().split())) for _ in range(2**n)]


l = list(map(int, input().split()))

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# 90도 돌리는 함수
def turn(si, sj, ei, ej):
    w = ei-si
    board = [[0] * w for _ in range(w)]

    for i in range(w):
        for j in range(w):
            board[j][w-1-i] = area[si+i][sj+j]

    for i in range(w):
        for j in range(w):
            area[si+i][sj+j] = board[i][j]


# 녹이기 함수
def melt():
    target = []
    size = 2**n
    for i in range(size):
        for j in range(size):
            if area[i][j] == 0:
                continue
            cnt = 0
            for d in range(4):
                ni, nj = i + di[d], j + dj[d]
                if 0 <= ni < size and 0 <= nj < size and area[ni][nj] > 0:
                    cnt += 1
            if cnt < 3:
                target.append((i, j))
    for i, j in target:
        area[i][j] -= 1

# 인접한 얼음 개수
def find(si, sj):
    q = deque()
    q.append([si, sj])
    visited[si][sj] = True

    cnt = 1
    while q:
        i, j = q.popleft()

        for d in range(4):
            ni, nj = i + di[d], j + dj[d]
            if 0 <= ni < 2**n and 0 <= nj < 2**n and not visited[ni][nj] and area[ni][nj] != 0:
                cnt += 1
                visited[ni][nj] = True
                q.append([ni, nj])

    return cnt

for size in l:
    k = 2**size
    for i in range(0, 2**n, k):
        for j in range(0, 2**n, k):
            turn(i, j, i+k, j+k)
    melt()

# for x in area:
#     print(x)

total_ice = sum(sum(x) for x in area)
biggest = 0
visited = [[False] * 2**n for _ in range(2**n)]
for i in range(2**n):
    for j in range(2**n):
        if area[i][j] != 0 and not visited[i][j]:
            biggest = max(biggest, find(i, j))

print(total_ice)
print(biggest)
