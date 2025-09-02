import sys
input = sys.stdin.readline

n = int(input())
files = [input().strip() for _ in range(n)]
if n == 1:
    print(files[0])
else:
    p = list(files[0])
    # print(p)

    for i in range(1, n):
        for j in range(len(p)):
            if p[j] != '?' and p[j] != files[i][j]:
                p[j] = '?'

    print(''.join(map(str, p)))
