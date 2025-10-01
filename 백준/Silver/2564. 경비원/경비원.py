import sys
input = sys.stdin.readline

w, h = map(int, input().split())
n = int(input())
info = [tuple(map(int, input().split())) for _ in range(n)]
me = tuple(map(int, input().split()))
# 1북 2남 3서 4동
# 왼쪽, 위가 기준

def get_pos(d, dist):
    if d == 1: # 북
        return dist
    elif d == 2: # 남
        return w + h + (w-dist)
    elif d == 3: # 서
        return 2 * w + h + (h-dist)
    elif d == 4:
        return w + dist

my_pos = get_pos(*me)
outline = 2 * (w + h)
res = 0
for d, dist in info:
    temp = get_pos(d, dist)
    diff = abs(my_pos - temp)
    res += min(diff, outline - diff)

print(res)