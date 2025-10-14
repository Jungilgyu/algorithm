
from itertools import permutations


f = list(map(str, input().split()))
m = list(map(str, input().split()))
p = f + m


child = set()
cases = permutations(p, 2)
for b, t in cases:
    child.add((b, t))

for c in p:
    child.add((c, c))

for b, t in sorted(child):
    print(b, t)


