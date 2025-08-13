import sys
from collections import deque

area = [list(map(str, input())) for _ in range(12)]

# for x in area:
#     print(x)
di = [0,1,0,-1]
dj = [1,0,-1,0]

ans = 0
# 4개 검사 4개 이상도 터뜨림
def sol(i, j):
    global ans
    q = deque()
    q.append([i, j])
    visited = [[False] * 6 for _ in range(12)]
    visited[i][j] = True
    res = [[i, j]]
    while q:
        x, y  = q.popleft()
        for k in range(4):
            nx, ny = x + di[k], y + dj[k]
            if 0 <= nx < 12 and 0 <= ny < 6:
                if area[nx][ny] == area[x][y] and not visited[nx][ny]:
                    q.append([nx, ny])
                    visited[nx][ny] = True
                    res.append([nx, ny])

    if len(res) >= 4:
        for x, y in res:
            area[x][y] = '.'
        return True

    return False



# 정렬
def sort():
    for i in range(11, -1, -1):
        for j in range(6):
            if area[i][j] != '.':
                down(i, j)


def down(i, j):
    current = area[i][j]

    next = i + 1
    while next < 12 and area[next][j] == '.':
        next += 1
    next -= 1

    if next == i:
        area[next][j] = current
    else:
        area[next][j] = current
        area[i][j] = '.'


ans = 0
while True:
    is_chain = False
    for i in range(11, -1, -1):
        for j in range(6):
            if area[i][j] != '.':
                if sol(i, j):
                    is_chain = True

    if is_chain:
        sort()
        ans += 1
    else:
        break

print(ans)


