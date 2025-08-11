import sys
input = sys.stdin.readline

n, m, l, k = map(int, input().split())
stars = [tuple(map(int, input().split())) for _ in range(k)]

x_candidates = set()
y_candidates = set()

for x, y in stars:
    x_candidates.add(x)
    if x - l >= 0:
        x_candidates.add(x - l)
    y_candidates.add(y)
    if y - l >= 0:
        y_candidates.add(y - l)

max_count = 0
for cx in x_candidates:
    for cy in y_candidates:
        count = 0

        for sx, sy in stars:
            if cx <= sx <= cx + l and cy <= sy <= cy + l:
                count += 1
        max_count = max(max_count, count)

print(k - max_count)