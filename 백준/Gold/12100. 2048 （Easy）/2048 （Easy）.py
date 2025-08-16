import sys

n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]

di = [0, 0, -1, 1] # 왼쪽, 오른쪽, 위, 아래
dj = [-1, 1, 0, 0]

def move(b, d): # 판, 방향
    if d == 0: # 왼쪽
        new_area = [] # 이동 후 최종 판형태
        for row in b:
            res = []
            temp = []
            for num in row:
                if num != 0:
                    temp.append(num)
            # 합치기
            visited = [False] * n
            for i in range(1, len(temp)):
                if temp[i] == temp[i-1] and not visited[i-1]:
                    temp[i-1] = temp[i-1] * 2
                    temp[i] = 0
                    visited[i-1] = True

            for x in temp:
                if x != 0:
                    res.append(x)
            # 빈칸채우기
            diff = n - len(res)
            res = res + [0] * diff
            new_area.append(res)

    elif d == 1: # 오른쪽
        new_area = [] # 이동 후 최종 판형태
        for row in b:
            res = []
            temp = []
            for num in row[::-1]:
                if num != 0:
                    temp.append(num)
            # 합치기
            visited = [False] * n
            for i in range(1, len(temp)):
                if temp[i] == temp[i-1] and not visited[i-1]:
                    temp[i-1] = temp[i-1] * 2
                    temp[i] = 0
                    visited[i-1] = True

            for x in temp:
                if x != 0:
                    res.append(x)
            # 빈칸채우기
            diff = n - len(res)
            res = res + [0] * diff
            new_area.append(res[::-1])

    # 위
    elif d == 2:
        new_area = [[0] * n for _ in range(n)]  # 이동 후 최종 판형태
        for i in range(n):
            res = []
            temp = []
            for j in range(n):
                if b[j][i] != 0:
                    temp.append(b[j][i])

            # 합치기
            visited = [False] * n
            for j in range(1, len(temp)):
                if temp[j] == temp[j - 1] and not visited[j - 1]:
                    temp[j - 1] = temp[j - 1] * 2
                    temp[j] = 0
                    visited[j - 1] = True

            for x in temp:
                if x != 0:
                    res.append(x)
            # 빈칸채우기
            diff = n - len(res)
            res = res + [0] * diff
            for j in range(n):
                new_area[j][i] = res[j]

    else: # 아래
        new_area = [[0] * n for _ in range(n)]  # 이동 후 최종 판형태
        for i in range(n):
            res = []
            temp = []
            for j in range(n-1, -1, -1):
                if b[j][i] != 0:
                    temp.append(b[j][i])

            # 합치기
            visited = [False] * n
            for j in range(1, len(temp)):
                if temp[j] == temp[j - 1] and not visited[j - 1]:
                    temp[j - 1] = temp[j - 1] * 2
                    temp[j] = 0
                    visited[j - 1] = True

            for x in temp:
                if x != 0:
                    res.append(x)
            # 빈칸채우기
            diff = n - len(res)
            res = res + [0] * diff
            for j in range(n):
                new_area[j][i] = res[n - j -1]

    return new_area

ans = 0
def sol(board, cnt):
    global ans
    if cnt == 5:
        max_val = max([max(x) for x in board])
        ans = max(max_val, ans)
        return

    for d in range(4):
        new_board = move(board, d)
        sol(new_board, cnt+1)

sol(area, 0)
print(ans)