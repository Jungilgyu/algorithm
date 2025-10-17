import sys
input = sys.stdin.readline

n = int(input())
words = [input().strip() for _ in range(n)]

unique = []

for w in words:
    is_new = True
    for u in unique:
        if len(u) == len(w) and w in (u + u):
            is_new = False
            break

    if is_new:
        unique.append(w)

print(len(unique))



