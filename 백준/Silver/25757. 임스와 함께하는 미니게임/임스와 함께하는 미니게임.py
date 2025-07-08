import sys
input = sys.stdin.readline
n, g = input().split()
p = [input() for _ in range(int(n))]
p  = list(set(p))

if g == 'Y':
    print(len(p))
elif g == 'F':
    print(len(p)//2)
else:
    print(len(p)//3)

