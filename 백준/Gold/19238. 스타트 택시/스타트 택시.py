import sys
from collections import deque
input = sys.stdin.readline

n, m, f = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]
si, sj = map(int, input().split())
si -= 1; sj -= 1

# 출발/목적 분리
start_id = [[0]*n for _ in range(n)]  # 출발지 손님 번호
dest = {}  # 손님번호 -> (ei, ej)

pnum = 2
for _ in range(m):
    pi, pj, ei, ej = map(int, input().split())
    start_id[pi-1][pj-1] = pnum
    dest[pnum] = (ei-1, ej-1)
    pnum += 1

complete = [False]*(m+5)
di, dj = [0,1,0,-1], [1,0,-1,0]

# 손님 찾기
def find_p(i, j, ff):
    q = deque()
    q.append((i, j, ff))
    visited = [[False]*n for _ in range(n)]
    visited[i][j] = True

    candidates = []
    min_d = float('inf')

    while q:
        ci, cj, cf = q.popleft()
        dist = ff - cf  # 소모한 연료 = 거리

        if cf < 0:  # 연료 바닥
            continue

        if dist > min_d:  # 더 먼 거리는 볼 필요 없음
            continue

        if start_id[ci][cj] > 0 and not complete[start_id[ci][cj]]:
            min_d = dist
            candidates.append((ci, cj, cf, start_id[ci][cj]))
            continue

        for k in range(4):
            ni, nj = ci+di[k], cj+dj[k]
            if 0<=ni<n and 0<=nj<n and not visited[ni][nj] and area[ni][nj]!=1:
                visited[ni][nj] = True
                q.append((ni, nj, cf-1))

    if not candidates:
        return -1

    # 거리(연료는 cf로 반영돼있음) → 행 → 열
    candidates.sort(key=lambda x: (ff-x[2], x[0], x[1]))
    ci, cj, cf, who = candidates[0]
    start_id[ci][cj] = 0  # 태운 자리 비우기
    return ci, cj, cf, who

# 목적지 이동
def to_dest(i, j, ff, who):
    q = deque()
    q.append((i, j, ff))
    visited = [[False]*n for _ in range(n)]
    visited[i][j] = True
    start_f = ff

    er, ec = dest[who]

    while q:
        ci, cj, cf = q.popleft()
        if cf < 0:
            continue

        if (ci, cj) == (er, ec):  # 도착
            used = start_f - cf
            ff = cf + used*2  # 연료 충전
            complete[who] = True
            return ci, cj, ff

        for k in range(4):
            ni, nj = ci+di[k], cj+dj[k]
            if 0<=ni<n and 0<=nj<n and not visited[ni][nj] and area[ni][nj]!=1:
                visited[ni][nj] = True
                q.append((ni, nj, cf-1))

    return -1

# 시뮬레이션
for _ in range(m):
    res1 = find_p(si, sj, f)
    if res1 == -1:
        print(-1); exit()
    si, sj, f, who = res1

    res2 = to_dest(si, sj, f, who)
    if res2 == -1:
        print(-1); exit()
    si, sj, f = res2

print(f)
