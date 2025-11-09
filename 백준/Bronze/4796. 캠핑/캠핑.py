import sys
input = sys.stdin.readline

c = 1
while True:
    l, p, v = map(int, input().split())
    if l == 0 and p == 0 and v == 0:
        break

    ans = 0

    ans += (v // p) * l + min((v % p), l)
    print(f'Case {c}: {ans}')
    c += 1






