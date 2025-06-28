import sys
from collections import deque

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
df = [-1, 1]

def bfs(f, i, j):
    q = deque()
    q.append([f, i, j, 0]) # 층수, x, y 좌표
    visited[f][i][j] = True

    while q:
        floor, x, y, cnt = q.popleft()

        if building[floor][x][y] == "E":
            return cnt

        for k in range(4):
            nx, ny = x + di[k], y + dj[k]
            if 0 <= nx < R and 0 <= ny < C and not visited[floor][nx][ny] and building[floor][nx][ny] != "#":
                q.append([floor, nx, ny, cnt + 1])
                visited[floor][nx][ny] = True

        for k in range(2):
            next_floor = floor + df[k]
            if 0 <= next_floor < L and not visited[next_floor][x][y] and building[next_floor][x][y] != "#":
                q.append([next_floor, x, y, cnt+1])
                visited[next_floor][x][y] = True
    return -1
while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break

    building = []
    start = None
    for l in range(L):
        floor = []
        for r in range(R):
            row = list(input().strip())
            for c in range(C):
                if row[c] == "S":
                    start = (l, r, c)
            floor.append(row)
        building.append(floor)
        input()

    visited = [[[False] * C for _ in range(R)] for _ in range(L)]

    ans = bfs(*start)

    if ans == -1:
        print("Trapped!")
    else:
        print(f"Escaped in {ans} minute(s).")


