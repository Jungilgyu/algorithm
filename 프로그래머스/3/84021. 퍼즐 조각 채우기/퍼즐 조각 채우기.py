from collections import deque
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def normalize(shape):
    shape.sort(key=lambda x: (x[0], x[1]))
    si, sj = shape[0]
    return [[i - si, j - sj] for i, j in shape]

def rotate(block):
    rotated = [[y, -x] for x, y in block]
    return normalize(rotated)

def check(block, cb, used):
    cb_norm = normalize(cb)
    temp = block
    for _ in range(4):
        temp = rotate(temp)
        if temp == cb_norm:
            return True
    return False

def find_block(si, sj, board, visited, n, m):
    q = deque()
    q.append([si, sj])
    visited[si][sj] = True
    res = [[si, sj]]
    while q:
        ci, cj = q.popleft()
        
        for k in range(4):
            ni, nj = ci + di[k], cj + dj[k]
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and board[ni][nj] == 1:
                q.append([ni, nj])
                res.append([ni, nj])
                visited[ni][nj] = True
    return res

def find_blank(si, sj, game_board, visited2, n, m):
    q = deque()
    q.append([si, sj])
    res = [[si, sj]]
    visited2[si][sj] = True
    while q:
        ci, cj = q.popleft()
        for k in range(4):
            ni, nj = ci + di[k], cj + dj[k]
            if 0 <= ni < n and 0 <= nj < m and game_board[ni][nj] == 0 and not visited2[ni][nj]:
                res.append([ni, nj])
                q.append([ni ,nj])
                visited2[ni][nj] = True
    return res

def solution(game_board, table):
    n = len(game_board)
    m = len(game_board[0])
    blocks = []
    visited = [[False] * m for _ in range(n)]
    
    # 블록찾기
    for i in range(n):
        for j in range(m):
            if table[i][j] == 1 and not visited[i][j]:
                blocks.append(find_block(i, j, table, visited, n, m))

    # 특정블록 사용여부  
    used = [False] * len(blocks) 
    # print(used)
    visited2 = [[False] * m for _ in range(n)]
    # 빈칸찾기 
    answer = 0
    for i in range(n):
        for j in range(m):
            if game_board[i][j] == 0 and not visited2[i][j]:
                cb = find_blank(i, j, game_board, visited2, n, m)
                cb.sort(key=lambda x: (x[0], x[1]))
                for l in range(len(blocks)):
                    if len(blocks[l]) == len(cb) and not used[l]:
                        if check(blocks[l], cb, used):
                            answer += len(cb)
                            used[l] = True 
                            break
                # print(cb)
        

    return answer