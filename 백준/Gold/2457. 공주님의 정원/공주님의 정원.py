import sys
input = sys.stdin.readline

n = int(input())
flowers = []
for _ in range(n):
    sm, sd, em, ed = map(int, input().split())
    flowers.append(((sm, sd), (em, ed)))

flowers.sort()

cur = (3, 1)  # 현재 커버해야 할 날짜
end = (11, 30)  # 목표
idx = 0
cnt = 0
best = (0, 0)

while cur <= end:
    picked = False
    # 현재 날짜 이전에 시작하는 꽃 중 가장 늦게 지는 꽃
    while idx < n and flowers[idx][0] <= cur:
        if flowers[idx][1] > best:
            best = flowers[idx][1]
        idx += 1
        picked = True

    if not picked:  # 이어질 꽃이 없음
        print(0)
        exit()

    cnt += 1
    cur = best  # 현재 범위 갱신


print(cnt)