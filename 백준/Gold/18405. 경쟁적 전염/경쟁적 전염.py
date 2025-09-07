import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]
time, end_i, end_j = map(int, input().split())

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs():
    q = deque()
    # 바이러스들 먼저 찾기
    virus = []
    for i in range(n):
        for j in range(n):
            if area[i][j] != 0:
                virus.append([area[i][j], i, j])

    virus.sort(key=lambda x: (x[0], x[1], x[2]))

    for v in virus:
        q.append([v[0], v[1], v[2], 0])

    while q:
        v_num, x, y, cnt = q.popleft()

        if cnt >= time:
            break

        for d in range(4):
            nx, ny = x + di[d], y + dj[d]
            if 0 <= nx < n and 0 <= ny < n and area[nx][ny] == 0:
                area[nx][ny] = v_num
                q.append([v_num, nx, ny, cnt + 1])

bfs()

print(area[end_i-1][end_j-1])

