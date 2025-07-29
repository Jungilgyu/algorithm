import sys
from collections import deque

T = int(input())

def sol(sx, sy, conv):
    q = deque()
    q.append([sx, sy])
    visited = [False] * (n+1)
    while q:
        x, y = q.popleft()

        if x == end_x and y == end_y and (abs(end_x - x) + abs(end_y - y)) <= 1000:
            print("happy")
            return

        for i in range(n+1):
            diff = abs(x-conv[i][0]) + abs(y-conv[i][1])
            if diff <= 1000 and not visited[i]:
                q.append([conv[i][0], conv[i][1]])
                visited[i] = True

    print("sad")
    return

for _ in range(T):
    n = int(input())
    start_x, start_y = map(int, input().split()) # 시작 위치
    conv = []
    for _ in range(n):
        x, y = map(int, input().split())
        conv.append([x, y])

    end_x, end_y = map(int, input().split())
    conv.append([end_x, end_y])
    sol(start_x, start_y, conv)














