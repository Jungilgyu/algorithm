import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    j, n = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(n)]
    box.sort(key=lambda x: x[0] * x[1], reverse=True)

    cnt = 0
    temp = 0
    for r, c in box:
        cnt += 1
        temp += r * c
        if temp >= j:
            print(cnt)
            break

