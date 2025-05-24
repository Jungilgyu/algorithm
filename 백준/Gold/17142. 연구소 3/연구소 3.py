import sys
from itertools import combinations
from collections import deque

n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# area에 바이러스가 k개 있을 때, 이 중에서 m개를 활성화 상태로 바꾸고,
# area 전체가 바이러스로 감염되기 까지의 시간이 가장 짧은 것을 구하기

def spread(lst):
    q = deque()
    temp = [[0] * n for _ in range(n)]
    for sx, sy in lst:
        q.append([sx, sy, 0])
        temp[sx][sy] = 1

    # 벽 표시
    for i in range(n):
        for j in range(n):
            if area[i][j] == 1:
                temp[i][j] = -1
            # 비활성화 바이러스 표시
            elif area[i][j] == 2 and [i, j] not in lst:
                temp[i][j] = -2

    empty_cnt = sum(row.count(0) for row in area)
    if empty_cnt == 0:
        return 0
    max_time = 0

    while q:
        x, y, time = q.popleft()

        for k in range(4):
            nx, ny = x + di[k], y + dj[k]
            if 0 <= nx < n and 0 <= ny < n:
                if temp[nx][ny] == 0:
                    temp[nx][ny] = 1
                    q.append([nx, ny, time + 1])
                    max_time = max(max_time, time+1)
                    empty_cnt -= 1
                elif temp[nx][ny] == -2:
                    temp[nx][ny] = 1
                    q.append([nx, ny, time + 1])


    if empty_cnt == 0:
        return max_time
    else:
        return False

# 0. area에서 바이러스들 좌표 찾기
viruses = []
for i in range(n):
    for j in range(n):
        if area[i][j] == 2:
            viruses.append([i, j])

answer = []
# 1. 조합 구하기
combs = combinations(viruses, m)
for comb in combs:
    res = spread(comb)
    if res is not False:
        answer.append(res)

if len(answer) == 0:
    print(-1)
else:
    print(min(answer))