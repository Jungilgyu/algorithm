import sys
input = sys.stdin.readline

n = int(input())
order = list(input().strip())

di = [1, 0, -1, 0] # 남 서 북 동
dj = [0, -1, 0, 1]

d = 0 # 현재 방향 (남쪽 시작)
si, sj = 0, 0 # 임의의 시작좌표 설정
route = set() # 지나온 길
route.add((si, sj))

for o in order:
    if o == 'L': # 왼쪽
        d = (d-1) % 4
    elif o == 'R':
        d = (d+1) % 4
    elif o == 'F':
        si += di[d]
        sj += dj[d]
        route.add((si, sj))

min_i = 51
max_i = -51
min_j = 51
max_j = -51
for i, j in route:
    min_i = min(min_i, i)
    max_i = max(max_i, i)
    min_j = min(min_j, j)
    max_j = max(max_j, j)

for i in range(min_i, max_i + 1):
    for j in range(min_j, max_j + 1):
        if (i, j) in route:
            print('.', end='')
        else:
            print('#', end='')

    print('')

