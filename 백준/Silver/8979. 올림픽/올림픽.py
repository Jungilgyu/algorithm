import sys

n, k = map(int, input().split())
ranking = [list(map(int, input().split())) for _ in range(n)]

ranking.sort(key=lambda x: (-x[1], -x[2], -x[3]))

rank = 1  
prev = ranking[0][1:]

for i in range(n):
    country, g, s, b = ranking[i]
    if [g, s, b] != prev:
        rank = i + 1  # 등수 갱신: 동점자 수만큼 점프
        prev = [g, s, b]
    if country == k:
        print(rank)
        break
