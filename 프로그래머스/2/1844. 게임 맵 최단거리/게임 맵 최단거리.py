from collections import deque

def bfs(maps):
    q = deque()
    
    n = len(maps)
    m = len(maps[0])
    
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    
    q.append([0, 0, 1])
    
    while q:
        i, j, cnt = q.popleft()
        
        if i == n-1 and j == m-1:
            return cnt
        
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and maps[ni][nj] == 1:
                q.append([ni, nj, cnt + 1])
                visited[ni][nj] = True
                
    return -1

def solution(maps):
    answer = bfs(maps)
    return answer