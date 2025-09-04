import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

board = [list(map(int, input().strip())) for _ in range(9)]

# 빈 칸 좌표 저장
blanks = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]

# 가로/세로/블록 체크 배열
row_used = [[False]*10 for _ in range(9)]
col_used = [[False]*10 for _ in range(9)]
box_used = [[False]*10 for _ in range(9)]

# 초기값 세팅
for i in range(9):
    for j in range(9):
        num = board[i][j]
        if num != 0:
            row_used[i][num] = True
            col_used[j][num] = True
            box_used[(i//3)*3 + j//3][num] = True

def dfs(idx):
    if idx == len(blanks):  # 모든 빈칸 채움
        for r in board:
            print(''.join(map(str, r)))
        sys.exit(0)

    x, y = blanks[idx]
    b = (x//3)*3 + y//3  # 블록 인덱스

    for num in range(1, 10):
        if not row_used[x][num] and not col_used[y][num] and not box_used[b][num]:
            # 숫자 넣기
            board[x][y] = num
            row_used[x][num] = col_used[y][num] = box_used[b][num] = True

            dfs(idx + 1)

            # 원상복구
            board[x][y] = 0
            row_used[x][num] = col_used[y][num] = box_used[b][num] = False

dfs(0)
