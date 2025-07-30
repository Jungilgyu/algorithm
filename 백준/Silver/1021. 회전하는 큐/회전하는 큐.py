import sys
from collections import deque

n, m = map(int, input().split())
targets = list(map(int, input().split()))

dq = deque(range(1, n + 1))  # 큐는 1부터 시작!
count = 0

for target in targets:
    idx = dq.index(target)  # 현재 deque에서 target의 위치
    if idx <= len(dq) // 2:
        # 왼쪽으로 rotate
        dq.rotate(-idx)
        count += idx
    else:
        # 오른쪽으로 rotate
        dq.rotate(len(dq) - idx)
        count += len(dq) - idx

    dq.popleft()  # 맨 앞 요소 제거

print(count)
