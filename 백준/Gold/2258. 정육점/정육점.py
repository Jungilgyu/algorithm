import sys
input = sys.stdin.readline

n, m = map(int, input().split())
meat = [tuple(map(int, input().split())) for _ in range(n)]

meat.sort(key=lambda x: (x[1], -x[0]))

total = 0       
ans = float('inf')
cnt = 0 # 같은 가격 개수 체크
prev_price = -1

for w, p in meat:
    if p == prev_price:
        cnt += 1  # 같은 가격이면 개수 추가
    else:
        cnt = 1   # 가격이 바뀌면 새로 시작
    total += w
    if total >= m:
        ans = min(ans, p * cnt)  # 같은 가격이면 cnt만큼 곱해야 함
    prev_price = p

print(ans if ans != float('inf') else -1)
