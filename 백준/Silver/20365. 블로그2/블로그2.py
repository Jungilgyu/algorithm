import sys
input = sys.stdin.readline

n = int(input())
target = input().strip()

r = list(target.split('B'))
b = list(target.split('R'))
r_cnt = 0
b_cnt = 0
for block in r:
    if block != '':
        r_cnt += 1
for block in b:
    if block != '':
        b_cnt += 1

print(min(r_cnt, b_cnt) + 1)
