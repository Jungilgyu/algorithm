import sys
input = sys.stdin.readline

N, L = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(N)]

ct = 0 # 시간
cl = 0 # 현재 위치

for l, r, g in info:
    # line 진입시 현재 line - 이전 line만큼 시간 추가
    ct += l - cl
    cl = l

    x = ct % (r+g)
    if x < r: # 빨간불에 걸림
        ct += r - x

ct += L - cl
print(ct)





