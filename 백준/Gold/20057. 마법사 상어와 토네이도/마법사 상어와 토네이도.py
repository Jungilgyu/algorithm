import sys

n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]

spread = [(-1, -1, 0.1), (-1, 0, 0.07),
          (-1, 1, 0.01), (-2, 0, 0.02),
          (0, -2, 0.05),
          (1, -1, 0.1), (1, 0, 0.07),
          (1, 1, 0.01), (2, 0, 0.02)]

di = [0, 1, 0, -1 ]
dj = [-1, 0, 1, 0]

def rotate(x, y, d):
    if d == 0:
        return x, y
    elif d == 1:
        return -y, x
    elif d == 2:
        return -x, -y
    elif d == 3:
        return y, -x

def sol(i, j, d):
    global ans
    # 현재 칸 모래량
    sand = area[i][j]
    area[i][j] = 0
    spread_sum = 0

    for x, y, r in spread:
        rx, ry = rotate(x, y, d)
        nx, ny = i + rx, j + ry
        amount = int(sand * r)
        spread_sum += amount
        if 0 <= nx < n and 0 <= ny < n:
            area[nx][ny] += amount
        else:
            ans += amount

    # 남은 모래
    ax, ay = i + di[d], j + dj[d]
    rest = sand - spread_sum
    if 0 <= ax < n and 0 <= ay < n:
        area[ax][ay] += rest
    else:
        ans += rest

    return

sx,sy = n//2, n//2
idx = 0
k = 1
ans = 0
while True:
    # k칸씩 진행
    for _ in range(2): # k칸씩 2번 진행함
        # 왼, 아 오, 위
        for _ in range(k):
            nx, ny = sx + di[idx], sy + dj[idx]
            sol(nx, ny, idx) # 모래뿌리기
            sx, sy = nx, ny
            if sx == 0 and sy == 0:
                print(ans)
                sys.exit()

        idx = (idx + 1) % 4
    k += 1

