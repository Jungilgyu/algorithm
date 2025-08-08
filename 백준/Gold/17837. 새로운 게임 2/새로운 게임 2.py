import sys
n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
# 0 흰색, 1 빨간색, 2 파란색
info = [[[] for _ in range(n)] for _ in range(n)]
horse = []
for num in range(k):
    i, j, d = map(int, input().split())
    info[i-1][j-1].append((num+1))
    horse.append([i-1, j-1, d-1])

# 방향 바꾸는 함수
def reverse_d(d):
    if d == 0:
        return 1
    elif d == 1:
        return 0
    elif d == 2:
        return 3
    else:
        return 2

def white(num, i, j, d):
    idx = info[i][j].index(num)
    move = info[i][j][idx:] # 움직일 말들
    ni, nj = i + di[d], j + dj[d] # 새로 이동할 곳 위치

    info[ni][nj].extend(move) # 움직일곳에 다 넣어

    # 그다음에 내 위에 있는 애들도 위치를 조정
    for h in move:
        horse[h-1][0], horse[h-1][1] = ni, nj  # 말 위치 갱신
    # 원래 자리는 이동한만큼 제거
    info[i][j] = info[i][j][:idx]

    return len(info[ni][nj]) >= 4


def red(num, i, j, d):
    idx = info[i][j].index(num)
    move = info[i][j][idx:][::-1]  # 내위로 뒤집어서 이동

    ni, nj = i + di[d], j + dj[d]  # 새로 이동할 곳 위치
    info[ni][nj].extend(move)  # 움직일곳에 다 넣어

    # 그다음에 내 위에 있는 애들도 위치를 조정
    for h in move:
        horse[h - 1][0], horse[h - 1][1] = ni, nj  # 말 위치 갱신
    # 원래 자리는 이동한만큼 제거
    info[i][j] = info[i][j][:idx]

    return len(info[ni][nj]) >= 4


di = [0, 0, -1, 1] # 오 왼 위 아
dj = [1, -1, 0, 0]

turn = 0
while turn < 1000:
    turn += 1
    for i in range(k):  # 말 번호 1번부터 k번까지
        x, y, d = horse[i]
        nx, ny = x + di[d], y + dj[d]  # 이동할 위치

        # 경계 밖이거나 파란색 칸
        if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] == 2:
            nd = reverse_d(d)  # 방향 반대
            horse[i][2] = nd  # 방향 갱신
            nx, ny = x + di[nd], y + dj[nd]  # 반대 방향으로 이동 시도
            if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] == 2:
                continue  # 이동 불가
            if board[nx][ny] == 0:  # 흰색
                if white(i + 1, x, y, nd):
                    print(turn)
                    exit()
            else:  # 빨간색
                if red(i + 1, x, y, nd):
                    print(turn)
                    exit()
        else:  # 흰색 또는 빨간색
            if board[nx][ny] == 0:
                if white(i + 1, x, y, d):
                    print(turn)
                    exit()
            else:
                if red(i + 1, x, y, d):
                    print(turn)
                    exit()

print(-1)