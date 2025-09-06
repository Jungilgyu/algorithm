import sys
from collections import deque
input = sys.stdin.readline

n, l = map(int, input().split())
lst = list(map(int, input().split()))

dq  = deque()
ans = []
for i in range(n):
    # 이게 dq[0]에 해당하는 값을 최소로 유지시킴
    while dq and lst[dq[-1]] > lst[i]:
        dq.pop()

    dq.append(i)

    # 범위 밖 제거 
    if dq[0] <= i - l:
        dq.popleft()

    ans.append(lst[dq[0]])

print(*ans)











