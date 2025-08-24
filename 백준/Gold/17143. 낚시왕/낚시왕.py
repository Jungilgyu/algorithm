import sys
input = sys.stdin.readline

r, c, m = map(int, input().split())
area = [[[] for _ in range(c)] for _ in range(r)]
shark = [] # i번 상어 정보
live = [1] * m # i번 상어 생존 여부
for i in range(m):
    sr, sc, s, d, z = map(int, input().split())
    shark.append([sr-1, sc-1, s, d, z])
    area[sr-1][sc-1].append(i)

# 방향전환  상어가 벽에 여러번 부딪힐 수 있음
def turn(d, s, i, j):
    # 위(1) / 아래(2)
    if d in (1, 2):
        if r == 1:                 # 세로 한 줄이면 못 움직임
            return i, j, d
        period = 2 * (r - 1)
        t = i if d == 2 else (period - i)   # 아래 시작은 i, 위 시작은 대칭점에서 시작
        t = (t + (s % period)) % period     # 왕복 선분에서 전진
        if t <= (r - 1):                    # 내려가는 구간
            return t, j, 2
        else:                               # 올라가는 구간
            return period - t, j, 1

    # 왼(4) / 오른(3)
    else:
        if c == 1:                 # 가로 한 줄이면 못 움직임
            return i, j, d
        period = 2 * (c - 1)
        t = j if d == 3 else (period - j)   # 오른쪽 시작은 j, 왼쪽 시작은 대칭점
        t = (t + (s % period)) % period
        if t <= (c - 1):                    # 오른쪽으로 가는 구간
            return i, t, 3
        else:                               # 왼쪽으로 가는 구간
            return i, period - t, 4




# 현재 낚시왕의 위치
current = 0
ans = 0
while current < c:
    # 가장 가까운 상어 하나 잡기
    for row in range(r):
        if area[row][current]: # 해당칸에 상어 있으면
            target = area[row][current][0] # 해당 상어의 번호
            ans += shark[target][4] # 해당상어 크기 추가
            live[target] = 0 # 해당 상어 죽이기
            area[row][current] = []
            break

    # 상어 이동
    temp = [[[] for _ in range(c)] for _ in range(r)] # 새로운 맵후보

    for i in range(m):
        if live[i]: # 살아있는 애들만 이동
            row, col, speed, direction, z = shark[i]
            next_row, next_col, next_d = turn(direction, speed, row, col)
            # 여기서 shark에 담을지 나중에 담을지
            shark[i] = [next_row, next_col, speed, next_d, z]
            if len(temp[next_row][next_col]): # 뭔가 들어있으면
                winner = temp[next_row][next_col][0] # 그중 가장 큰 애
                if z > shark[winner][4]: # 현재 상어가 더 크면
                    live[winner] = 0 # 걔 죽이고
                    temp[next_row][next_col] = [i]
                else:
                    live[i] = 0
            else:
                temp[next_row][next_col].append(i)


    # 상어판 교체
    area[:] = temp
    current += 1


print(ans)