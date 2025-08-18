import sys

cases = []
while True:
    line = input().strip()
    if line == "end":
        break
    cases.append(line)

def is_win(board, player):
    # 가로
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
    # 세로
    for j in range(3):
        if all(board[i][j] == player for i in range(3)):
            return True
    # 대각선
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def sol(board):
    x_cnt = sum(row.count('X') for row in board)
    o_cnt = sum(row.count('O') for row in board)

    # 1. 개수 조건
    if o_cnt > x_cnt:
        return False
    if x_cnt > o_cnt + 1:
        return False

    x_win = is_win(board, 'X')
    o_win = is_win(board, 'O')

    # 2. 둘 다 이기는 경우 → invalid
    if x_win and o_win:
        return False

    # 3. 승자에 따른 개수 조건
    if x_win and x_cnt != o_cnt + 1:
        return False
    if o_win and x_cnt != o_cnt:
        return False

    # 4. 승자가 없는 경우 → 꽉 차야 함
    if not x_win and not o_win:
        if x_cnt + o_cnt != 9:
            return False

    return True

for line in cases:
    board = [[line[i*3 + j] for j in range(3)] for i in range(3)]
    print("valid" if sol(board) else "invalid")
