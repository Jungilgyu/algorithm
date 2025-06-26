import sys
from collections import deque

R, C, N = map(int, input().split())

# area = [list(map(str, input())) for _ in range(R)]
area = [list(input().strip()) for _ in range(R)]
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

target = deque()
for i in range(R):
    for j in range(C):
        if area[i][j] == "O":
            target.append([i, j])

for i in range(1, N):
    if i % 2 == 1:
        area = [["O"] * C for _ in range(R)]

    else:
        while target:
            x, y = target.popleft()
            area[x][y] = "."
            for k in range(4):
                nx, ny = x + di[k], y + dj[k]
                if 0 <= nx < R and 0 <= ny < C and area[nx][ny] == "O":
                    area[nx][ny] = "."

        for l in range(R):
            for m in range(C):
                if area[l][m] == "O":
                    target.append([l, m])
for x in area:
    print("".join(map(str, x)))


