import sys
from itertools import permutations
input = sys.stdin.readline

n, m, k = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]
command = [list(map(int, input().split())) for _ in range(k)]

def rotate(r, c, s, board):
    arr = [row[:] for row in board]
    r -= 1
    c -= 1
    for d in range(1, s+1):
        top, bottom = r-d, r+d
        left, right = c-d, c+d
        prev = arr[top][left]

        for col in range(left+1, right+1):
            arr[top][col], prev = prev, arr[top][col]
        for row in range(top + 1, bottom + 1):
            arr[row][right], prev = prev, arr[row][right]
        for col in range(right - 1, left - 1, -1):
            arr[bottom][col], prev = prev, arr[bottom][col]
        for row in range(bottom - 1, top - 1, -1):
            arr[row][left], prev = prev, arr[row][left]
    return arr

ans = float('inf')
for case in permutations(command):
    temp = [row[:] for row in area]
    for r, c, s in case:
        temp = rotate(r, c, s, temp)
    ans = min(ans, min(sum(row) for row in temp))

print(ans)


