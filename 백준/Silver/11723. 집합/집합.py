import sys
input = sys.stdin.readline

m = int(input())
s = set()
for _ in range(m):
    v = input().split()
    opr, n = -1, -1
    if len(v) == 2:
        opr, n = v[0], int(v[1])
    else:
        opr = v[0]

    if opr == "add":
        s.add(n)
    elif opr == "remove":
        if n in s:
            s.remove(n)
    elif opr == "check":
        if n in s:
            print(1)
        else:
            print(0)
    elif opr == "toggle":
        if n in s:
            s.remove(n)
        else:
            s.add(n)
    elif opr == "all":
        s = {i for i in range(1, 21)}
    else:
        s = set()


