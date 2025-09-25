import sys
input = sys.stdin.readline

n = int(input())
info = {}
for _ in range(n):
    name, d, m, y = input().split()
    info[name] = [int(y), int(m), int(d)]

sorted_items = sorted(info.items(), key=lambda x: (x[1][0], x[1][1], x[1][2]))

print(sorted_items[-1][0])
print(sorted_items[0][0])

