import sys
input = sys.stdin.readline

n = int(input())
toping = list(input().split())
c = set()
for t in toping:
    if t.endswith('Cheese'):
        c.add(t)
if len(c) >= 4:
    print('yummy')
else:
    print('sad')





