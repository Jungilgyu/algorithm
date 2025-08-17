import sys

from collections import deque
import copy

di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, -1, -1, -1, 0, 1, 1, 1]

# . 물고기 이동 함수
def fish_move(area):
    move_complete = [False] * 17
    for fish_num in range(1, 17):
        for i in range(4):
            for j in range(4):
                if area[i][j][0] == fish_num and live_fish[fish_num] and not move_complete[fish_num]:
                    move_complete[fish_num] = True
                    x, y, dir = i, j, area[i][j][1]
                    # 물고기가 가장 먼저 이동판별할 위치는 d방향
                    d = dir - 1
                    for _ in range(8): # while로 찾을 필요없이 주변탐색은 최대 8번임
                        nx, ny = x + di[d], y + dj[d]
                        if 0 <= nx < 4 and 0 <= ny < 4 and area[nx][ny][0] != "shark":
                            area[nx][ny], area[x][y] = area[x][y], area[nx][ny]
                            # 방향튼 후에 위치를 바꾸는 경우면 튼 각도를 반영해줘야지
                            area[nx][ny][1] = d + 1 ## 이걸 계속 빼먹고 있어음  ㅠ
                            break
                        else:
                            d = (d+1) % 8
                    break
def shark_move(area, x, y, cnt):
    global ans
    case = copy.deepcopy(area)
    dead_fish = case[x][y][0]
    if dead_fish != "empty":  # 상어가 먹을 물고기가 있을 때만 처리
        live_fish[dead_fish] = False
        cnt += dead_fish
        case[x][y][0] = "shark"
        fish_move(case)
        ans = max(ans, cnt)
        d = case[x][y][1] - 1
        for k in range(1, 4):
            nx, ny = x + k * di[d], y + k * dj[d]
            if 0 <= nx < 4 and 0 <= ny < 4 and case[nx][ny][0] != "empty":
                temp_fish = case[nx][ny][0]
                case[x][y][0] = "empty"
                shark_move(case, nx, ny, cnt)
                case[x][y][0] = dead_fish  # 원상태로 복구
                live_fish[temp_fish] = True  # 이동했던 물고기 다시 복구


# 이부분 다시 생각해봐

area = [[] for _ in range(4)]
# print(area)
for i in range(4):
    arr = list(map(int, input().split()))
    # print(arr)
    idx = 0
    while idx < 8:
        a, b = arr[idx], arr[idx + 1]
        area[i].append([a, b])
        idx += 2

# 물고기 생존 여부 표시
live_fish = [True] * 17
ans = 0
shark_move(area, 0, 0, 0)
# for m in area:
#     print(m)
# 상어 움직임 함수 다시 생각해보기
print(ans)