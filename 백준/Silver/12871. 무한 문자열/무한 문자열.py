import sys
input = sys.stdin.readline

s = input().strip()
t = input().strip()

if len(s) == len(t):
    if s == t:
        print(1)
    else:
        print(0)
else:
    c = len(s) * len(t)
    S = s * (c // len(s))
    T = t * (c // len(t))

    if S == T:
        print(1)
    else:
        print(0)






