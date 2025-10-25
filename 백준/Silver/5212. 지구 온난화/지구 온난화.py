import sys
input = sys.stdin.readline

r, c = map(int, input().split())
area = [list(input().strip()) for _ in range(r)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

target = []
for i in range(r):
    for j in range(c):
        if area[i][j] == 'X':
            cnt = 0
            for k in range(4):
                ni, nj = i + di[k], j + dj[k]
                # 범위내에 있는데 .인경우
                if 0 <= ni < r and 0 <= nj < c and area[ni][nj] == 'X':
                    continue
                else:
                    cnt += 1

            if cnt >= 3:
                target.append([i, j])

for ti, tj in target:
    area[ti][tj] = '.'

left, right, top, bottom = 11, -1, 11, -1
for i in range(r):
    for j in range(c):
        if area[i][j] == 'X':
            left = min(left, j)
            right = max(right, j)
            top = min(top, i)
            bottom = max(top, i)

for i in range(top, bottom+1):
    print(''.join(map(str, area[i][left:right+1])))










