import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

# (r, c, m, s, d)
fireballs = [tuple(map(int, input().split())) for _ in range(m)]
# 인덱스 보정 (문제는 1-based)
fireballs = [(r-1, c-1, m, s, d) for r, c, m, s, d in fireballs]

di = [-1,-1,0,1,1,1,0,-1]
dj = [0,1,1,1,0,-1,-1,-1]

for _ in range(k):
    # 1. 이동
    new_map = {}
    for r, c, m, s, d in fireballs:
        nr = (r + s*di[d]) % n
        nc = (c + s*dj[d]) % n
        if (nr, nc) not in new_map:
            new_map[(nr, nc)] = []
        new_map[(nr, nc)].append((m, s, d))

    # 2. 합치고 분리
    new_fireballs = []
    for (r, c), balls in new_map.items():
        if len(balls) == 1:  # 그대로 유지
            m, s, d = balls[0]
            new_fireballs.append((r, c, m, s, d))
        else:  # 합치기
            m_sum = sum(b[0] for b in balls)
            s_sum = sum(b[1] for b in balls)
            cnt = len(balls)
            new_m = m_sum // 5
            if new_m == 0:
                continue
            new_s = s_sum // cnt

            # 방향 판별
            evens = sum(1 for b in balls if b[2] % 2 == 0)
            odds = cnt - evens
            if evens == cnt or odds == cnt:
                dirs = [0, 2, 4, 6]
            else:
                dirs = [1, 3, 5, 7]

            for d in dirs:
                new_fireballs.append((r, c, new_m, new_s, d))

    fireballs = new_fireballs

# 3. 결과 출력
print(sum(f[2] for f in fireballs))
