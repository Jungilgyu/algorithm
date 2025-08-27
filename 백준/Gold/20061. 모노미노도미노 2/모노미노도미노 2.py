import sys
input = sys.stdin.readline

n = int(input())
order = [list(map(int, input().split())) for _ in range(n)]

blue = [[0] * 4 for _ in range(6)]
green = [[0] * 4 for _ in range(6)]

def to_blue(num, i, j, board):
    nj = 3 - i
    if num in (1, 2): # ㅡ 모양
        row = -1
        while row < 5:
            next_row = row + 1
            if board[next_row][nj] == 0:
                row = next_row
            else:
                break
        if num == 1: # 1번 블록
            board[row][nj] = 1
        else: # 2번 블록
            board[row-1][nj], board[row][nj] = 1, 1 # 블록 놓기

    else: # l 모양 , 3번 블록
        nnj = nj -1
        row = -1
        while row < 5:
            next_row = row + 1
            if board[next_row][nj] == 0 and board[next_row][nnj] == 0:
                row = next_row
            else:
                break
        board[row][nj], board[row][nnj] = 1, 1  # 블록 놓기

    compress(board)
    for _ in range(check(board)):
        push(board)

def to_green(num, i, j, board):
    if num in (1, 2):
        row = -1
        if num == 1:  # 1번 블록
            while row < 5:
                next_row = row + 1
                if board[next_row][j] == 0:
                    row = next_row
                else:
                    break
            board[row][j] = 1

        else:  # 2번 블록
            while row < 5:
                next_row = row + 1
                if board[next_row][j] == 0 and board[next_row][j+1] == 0:
                    row = next_row
                else:
                    break
            board[row][j], board[row][j+1] = 1, 1  # 블록 놓기

    else: # 3번블록
        row = -1
        while row < 5:
            next_row = row + 1
            if board[next_row][j] == 0:
                row = next_row
            else:
                break
        board[row-1][j], board[row][j] = 1, 1  # 블록 놓기

    compress(board)
    for _ in range(check(board)):
        push(board)

# 압축하기
def compress(board):
    global ans
    # 연쇄작용 있을수도 있음
    while True:
        cnt = 0
        for i in range(5, 1, -1):# 아래서부터 검사
            if sum(board[i]) == 4: # 해당 줄이 꽉 차면 당겨주기
                new_board = [[0,0,0,0]] + board[:i] + board[i+1:]
                board[:] = new_board
                ans += 1 # 점수 1점 증가
                break # 처음부터 다시 검사
            else:
                cnt += 1
        if cnt == 4: # 줄삭제 필요없는개 4개 => while종료
            break

# 바닥으로 밀기
def push(board):
    new_board = [[0, 0, 0, 0]] + board[:5]
    board[:] = new_board

def check(board):
    cnt = 0
    for i in range(2):
        for j in range(4):
            if board[i][j] == 1:
                cnt += 1
                break
    return cnt

ans = 0
# 시뮬
for o in order:
    num, i, j = o
    to_blue(num, i, j, blue)
    to_green(num, i, j, green)


res_cnt = 0
for i in range(2, 6):
    for j in range(4):
        if blue[i][j] == 1:
            res_cnt += 1
        if green[i][j] == 1:
            res_cnt += 1
print(ans)
print(res_cnt)

# print("파랑")
# for x in blue:
#     print(x)
#
# print("초록")
# for x in green:
#     print(x)