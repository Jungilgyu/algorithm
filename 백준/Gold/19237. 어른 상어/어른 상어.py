import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

# 상어 위치 기록
area_shark = [list(map(int, input().split())) for _ in range(n)]
sd = list(map(int, input().split()))  # 상어의 방향 (1~4)
sdp = [[] for _ in range(m)]  # 방향 우선순위

for i in range(m):
    for _ in range(4):
        d = list(map(int, input().split()))
        sdp[i].append(d)

# 상어 냄새 기록 (상어번호, 남은시간)
area_smell = [[[] for _ in range(n)] for _ in range(n)]

# 상, 하, 좌, 우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

# 상어 초기 위치
si = []
for i in range(n):
    for j in range(n):
        if area_shark[i][j] != 0:
            si.append([area_shark[i][j], i, j])

# 상어 생존 여부
live = [1] * m

# 격자에 생존한 상어 수 확인
def check():
    return sum(live) == 1

# 현재 위치에 냄새 뿌리기 (k만큼 지속)
def spread():
    for i in range(n):
        for j in range(n):
            if area_shark[i][j] != 0:
                sn = area_shark[i][j]
                area_smell[i][j] = [sn, k]

# 우선순위에 따라 이동 좌표 리턴
def priority(num, candidates, i, j):
    cd = sd[num - 1]  # 현재 방향
    order = sdp[num - 1][cd - 1]

    # 위치정보만 저장
    candi = []
    for x, y, _ in candidates:
        candi.append((x, y))

    for nd in order:
        ni, nj = i + di[nd - 1], j + dj[nd - 1]
        if 0 <= ni < n and 0 <= nj < n and (ni, nj) in candi:
            return ni, nj, nd  # 우선순위에 맞는 방향 반환


# 방향 정하기
def direction(num, i, j):
    # 1. 주변에 빈 칸 탐색
    blank_lst = []
    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < n and 0 <= nj < n and area_shark[ni][nj] == 0 and not area_smell[ni][nj]:
            blank_lst.append([ni, nj, k+1])

    if blank_lst:  # 빈칸 있으면 우선순위 따라 이동
        if len(blank_lst) == 1:
            return blank_lst[0]
        return priority(num, blank_lst, i, j)

    # 2. 자기 냄새가 있는 칸 탐색
    same_smell = []
    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < n and 0 <= nj < n and area_smell[ni][nj] and area_smell[ni][nj][0] == num:
            same_smell.append([ni, nj, k+1])

    if same_smell:
        if len(same_smell) == 1:
            return same_smell[0]
        return priority(num, same_smell, i, j)

    # 3. 그냥 인접칸 중 하나
    adj_lst = []
    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < n and 0 <= nj < n:
            adj_lst.append([ni, nj, k+1])
    return priority(num, adj_lst, i, j)

# 상어 이동
def move():
    temp = [[[] for _ in range(n)] for _ in range(n)]
    lst = []

    for s in si:
        num, i, j = s
        if live[num-1] == 1:
            ni, nj, next_d = direction(num, i, j)
            lst.append([num, ni, nj, next_d])
            temp[ni][nj].append(num)

    # 격자 리셋
    for i in range(n):
        for j in range(n):
            area_shark[i][j] = 0

    new_si = []
    for num, i, j, d in lst:
        if live[num-1] == 1:
            if temp[i][j]:
                winner = min(temp[i][j])
                for loser in temp[i][j]:
                    if loser != winner:
                        live[loser-1] = 0
                if num == winner:
                    area_shark[i][j] = num
                    sd[num-1] = d
                    new_si.append([num, i, j])
    si[:] = new_si

# 냄새 1씩 줄이기
def minus():
    for i in range(n):
        for j in range(n):
            if area_smell[i][j]:
                area_smell[i][j][1] -= 1
                if area_smell[i][j][1] == 0:
                    area_smell[i][j] = []

ans = 0
spread()  # 초기 냄새 먼저 뿌려줌

for _ in range(1000):
    ans += 1
    move()
    minus()
    spread()
    if check():
        break

print(ans if check() else -1)
