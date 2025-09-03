import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, h = map(int, input().split())
if m == 0:
    print(0)
    exit()

board = [[0] * n for _ in range(h)]
for _ in range(m):
    a, b = map(int, input().split())
    board[a-1][b-1] = 1

def check(return_count=False):
    matched = 0
    for start in range(n):
        j = start
        for i in range(h):
            if j > 0 and board[i][j-1] == 1:
                j -= 1
            elif j < n-1 and board[i][j] == 1:
                j += 1
        if j == start:
            matched += 1
    if return_count:
        return matched
    return matched == n

ans = 4

def sol(count, row, col, max_cnt):
    global ans

    # 현재까지 맞은 세로선 수
    matched = check(return_count=True)
    if matched + (max_cnt - count) * 2 < n:
        return  # 남은 시도로도 모든 세로선을 맞출 수 없으면 중단

    if check():
        ans = min(ans, count)
        return

    if count == max_cnt or count >= ans:
        return

    for i in range(row, h):
        k = col if i == row else 0
        for j in range(k, n-1):
            if board[i][j] == 0 and board[i][j+1] == 0:
                # 인접 체크
                if j > 0 and board[i][j-1] == 1:
                    continue
                if j < n-2 and board[i][j+1] == 1:
                    continue
                board[i][j] = 1
                sol(count+1, i, j+2, max_cnt)  
                board[i][j] = 0

# 최대 0~3개 추가하는 경우를 모두 시도
found = False
for max_cnt in range(4):
    sol(0, 0, 0, max_cnt)
    if ans != 4:
        found = True
        break

print(ans if found else -1)
