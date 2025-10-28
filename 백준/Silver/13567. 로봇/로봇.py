import sys
input = sys.stdin.readline

m, n = map(int, input().split())

orders = [list(input().split()) for _ in range(n)]

# 시작은 동쪽
di = [0, -1, 0, 1]
dj = [1, 0, -1, 0]

def sol(si, sj, d):

    for order, num in orders:
        if order == 'TURN':
            if num == '0': #왼쪽 90도
                d = (d-1) % 4
            elif num == '1':
                d = (d+1) % 4
        elif order == 'MOVE':
            ni, nj = si + di[d] * int(num), sj + dj[d] * int(num)
            if 0 <= ni < m and 0 <= nj < m:
                si, sj = ni, nj
            else:
                return False

    return si, sj

res = sol(0, 0, 0)
if res == False:
    print(-1)
else:
    y, x = res
    print(x, y)

