

n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]

res = []
for i in range(n): # 50
    rank = 1
    x, y = info[i]
    for j in range(n): # 50
        if i != j:
            p, q = info[j]
            if p > x and q > y:
                rank += 1
    res.append(rank)

print(*res)

