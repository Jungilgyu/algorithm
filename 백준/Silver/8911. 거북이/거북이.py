import sys
input = sys.stdin.readline

T = int(input())

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def sol(com):
    sx, sy = 0, 0
    d = 0

    min_x, min_y, max_x, max_y = 0, 0, 0, 0
    for c in com:
        if c == 'L':
            d = (d - 1) % 4
        elif c == 'R':
            d = (d + 1) % 4
        elif c == 'F':
            sx, sy = sx + dx[d], sy + dy[d]
        elif c == 'B':
            sx, sy = sx - dx[d], sy - dy[d]

        # 갱신
        min_x = min(min_x, sx)
        min_y = min(min_y, sy)
        max_x = max(max_x, sx)
        max_y = max(max_y, sy)

    w = max_x - min_x
    h = max_y - min_y
    return w * h


for tc in range(T):
    command = input().strip()

    print(sol(command))






