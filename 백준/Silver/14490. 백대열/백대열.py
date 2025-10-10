import sys
input = sys.stdin.readline

a, b = map(int, input().split(':'))


def sol(a, b):
    res = -1
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            res = i

    if res != -1:
        print(f'{a//res}:{b//res}')
    else:
        print(f'{a}:{b}')

sol(a, b)




