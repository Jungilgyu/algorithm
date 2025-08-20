import sys
from collections import deque


# 입력
n, m, f = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]   
si, sj = map(int, input().split())
si -= 1; sj -= 1  

start_id = [[0]*n for _ in range(n)]
passengers = {}  

pnum = 2
for _ in range(m):
    sr, sc, er, ec = map(int, input().split())
    sr -= 1; sc -= 1; er -= 1; ec -= 1
    start_id[sr][sc] = pnum         # 출발지에 손님 번호 기록
    passengers[pnum] = (er, ec)     # 목적지 기록
    pnum += 1

complete = [False] * (m + 5)
di, dj = [0, 1, 0, -1], [1, 0, -1, 0]

# 손님 찾기
def find_p(i, j, fuel):
    q = deque()
    q.append((i, j))
    dist = [[-1]*n for _ in range(n)]
    dist[i][j] = 0
    targets = []
    min_d = float('inf')

    while q:
        ci, cj = q.popleft()
        d = dist[ci][cj]

        if d > min_d:
            continue

        if start_id[ci][cj] > 0 and not complete[start_id[ci][cj]]:
            if d < min_d:
                min_d = d
                targets = [(d, ci, cj, start_id[ci][cj])]
            elif d == min_d:
                targets.append((d, ci, cj, start_id[ci][cj]))
            continue

        for k in range(4):
            ni, nj = ci + di[k], cj + dj[k]
            if 0 <= ni < n and 0 <= nj < n and area[ni][nj] != 1 and dist[ni][nj] == -1:
                dist[ni][nj] = d + 1
                q.append((ni, nj))

    if not targets:
        return -1

    # 거리 같으면 행, 열 순서
    targets.sort(key=lambda x: (x[0], x[1], x[2]))
    d, pi, pj, pnum = targets[0]

    if fuel < d:
        return -1

    # 손님 태움 → 출발지 칸 비우기
    start_id[pi][pj] = 0
    return pi, pj, fuel - d, pnum

# 목적지로 이동
def to_dest(i, j, fuel, pnum):
    er, ec = passengers[pnum]
    q = deque()
    q.append((i, j))
    dist = [[-1]*n for _ in range(n)]
    dist[i][j] = 0

    while q:
        ci, cj = q.popleft()
        d = dist[ci][cj]

        if (ci, cj) == (er, ec):

            if fuel < d:
                return -1
            # 도착하면 소모량*2 충전
            fuel = fuel - d + (d * 2)  # = fuel + d
            complete[pnum] = True
            return ci, cj, fuel

        for k in range(4):
            ni, nj = ci + di[k], cj + dj[k]
            if 0 <= ni < n and 0 <= nj < n and area[ni][nj] != 1 and dist[ni][nj] == -1:
                dist[ni][nj] = d + 1
                q.append((ni, nj))

    return -1


for _ in range(m):
    res = find_p(si, sj, f)
    if res == -1:
        print(-1); sys.exit(0)
    si, sj, f, who = res

    res2 = to_dest(si, sj, f, who)
    if res2 == -1:
        print(-1); sys.exit(0)
    si, sj, f = res2

print(f)
