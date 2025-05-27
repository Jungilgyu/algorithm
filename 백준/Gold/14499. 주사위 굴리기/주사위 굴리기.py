import sys

n, m, sx, sy, k = map(int, input().split())

area = []
for _ in range(n):
    row = list(map(int, input().split()))
    area.append(row)


orders = list(map(int, input().split()))

di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]
# 1동, 2서, 3북, 4남

# dice = [1, 2, 3, 4, 5, 6]
# 남쪽  2 6 3 4 1 5
# 북쪽  5 1 3 4 6 2
# 동쪽  4 2 1 6 5 3
# 서쪽  3 2 6 1 5 4

def change_dice(dice, direction):
    one, two, three, four, five, six = dice
    if direction == 1: #동쪽
        dice = [four, two, one, six, five, three]
    elif direction == 2: #서쪽
        dice = [three, two, six, one, five, four]
    elif direction == 3: #북쪽
        dice = [five, one, three, four, six, two]
    else:
        dice = [two, six, three, four, one, five]

    return dice

dice = [0, 0, 0, 0, 0, 0]
# dice = [1, 2, 3, 4, 5, 6]
#
# dice = change_dice(dice, 1)
# print(dice)
for d in orders:
    nx, ny = sx + di[d-1], sy + dj[d-1]
    if 0 <= nx < n and 0 <= ny < m:
        # 주사위를 먼저 굴려
        dice = change_dice(dice, d)
        # 시작 위치 바꿔주기
        sx, sy = nx, ny

        if area[nx][ny] == 0:
            area[nx][ny] = dice[5]
        else:
            dice[5] = area[nx][ny]
            area[nx][ny] = 0

        print(dice[0])




