import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())

    p = [input().strip() for _ in range(n)]
    p.sort()

    ans = True
    for i in range(n - 1):
        if p[i + 1].startswith(p[i]):
            ans = False
            break

    print("YES" if ans else "NO")


















