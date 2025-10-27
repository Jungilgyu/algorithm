import sys
input = sys.stdin.readline

h, w = map(int, input().split())
area = [list(input().strip()) for _ in range(h)]

ans = [[-1] * w for _ in range(h)]

for i in range(h):
    for j in range(w):
        if area[i][j] == '.':
            find = False
            cnt = 0
            col = j
            while col > 0:
                col -= 1
                cnt += 1
                if area[i][col] == 'c':
                    find = True
                    break

            if find:
               ans[i][j] = cnt

        elif area[i][j] == 'c':
            ans[i][j] = 0

for x in ans:
    print(*x)





