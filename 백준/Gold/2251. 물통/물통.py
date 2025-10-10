import sys
from collections import deque
input = sys.stdin.readline

A, B, C = map(int, input().split())
visited = [[False] * (B + 1) for _ in range(A + 1)]

# a, b, c 에서 만들 수 있는 다음 상태
def move(a, b, c):
    res = []
    # A, B, C는 총용량
    # a, b, c는 현재 있는 물의 양
    # A > B
    p = min(a, B-b)
    res.append((a-p, b+p, c))
    # A > C
    p = min(a, C-c)
    res.append((a-p, b, c+p))
    # B > A
    p = min(b, A-a)
    res.append((a+p, b-p, c))
    # B > C
    p = min(b, C-c)
    res.append((a, b-p, c+p))
    # C > A
    p = min(c, A-a)
    res.append((a+p, b, c-p))
    # C > B
    p = min(c, B-b)
    res.append((a, b+p, c-p))
    return res

def bfs():
    q = deque()
    q.append([0, 0, C])
    visited[0][0] = True
    ans = set()

    while q:
        a, b, c = q.popleft()
        if a == 0:
            ans.add(c)

        for na, nb, nc in move(a, b, c):
            # move에선 한번 움직인 것만 처리하고
            # a->b->c 같이 2번이상 섞는건 while루프 돌면서 알아서
            if not visited[na][nb]:
                visited[na][nb] = True
                q.append((na, nb, nc))

    return ans
print(*sorted(bfs()))



