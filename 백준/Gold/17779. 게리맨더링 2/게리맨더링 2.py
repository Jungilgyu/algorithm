import sys
input = sys.stdin.readline

n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]
ans = 10**18

def solve(x, y, d1, d2):
    mark = [[0]*n for _ in range(n)]

    # 경계선 5번 표시
    for i in range(d1+1):
        mark[x+i][y-i] = 5
        mark[x+d2+i][y+d2-i] = 5
    for i in range(d2+1):
        mark[x+i][y+i] = 5
        mark[x+d1+i][y-d1+i] = 5

    # 경계선 안쪽 채우기
    for r in range(x+1, x+d1+d2):
        flag = False
        for c in range(n):
            if mark[r][c] == 5:
                flag = not flag
            if flag:
                mark[r][c] = 5

    population = [0]*5

    # 1번 구역
    for r in range(x+d1):
        for c in range(y+1):
            if mark[r][c] == 5:
                break
            population[0] += area[r][c]

    # 2번 구역
    for r in range(x+d2+1):
        for c in range(n-1, y, -1):
            if mark[r][c] == 5:
                break
            population[1] += area[r][c]

    # 3번 구역
    for r in range(x+d1, n):
        for c in range(y-d1+d2):
            if mark[r][c] == 5:
                break
            population[2] += area[r][c]

    # 4번 구역
    for r in range(x+d2+1, n):
        for c in range(n-1, y-d1+d2-1, -1):
            if mark[r][c] == 5:
                break
            population[3] += area[r][c]

    # 5번 구역
    total = sum(map(sum, area))
    population[4] = total - sum(population[:4])

    return max(population) - min(population)


for x in range(n):
    for y in range(n):
        for d1 in range(1, n):
            for d2 in range(1, n):
                if x+d1+d2 >= n: continue
                if y-d1 < 0 or y+d2 >= n: continue
                ans = min(ans, solve(x, y, d1, d2))

print(ans)
