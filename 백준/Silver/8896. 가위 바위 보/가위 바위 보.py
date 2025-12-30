import sys

def loser(a, b):
    if (a, b) in [('R', 'S'), ('S', 'P'), ('P', 'R')]:
        return b
    else:
        return a

T = int(input())
for tc in range(T):
    n = int(input())
    robots = list(input().strip() for _ in range(n))
    k = len(robots[0])

    alive = list(range(n))

    for t in range(k):
        if len(alive) == 1:
            break

        moves = set(robots[i][t] for i in alive)


        if len(moves) == 2:
            a, b = tuple(moves)
            l = loser(a, b)
            alive = [i for i in alive if robots[i][t] != l]

    print(alive[0] + 1 if len(alive) == 1 else 0)

    # print(k)
    # print(robots)

    # 1. 가위바위보 비교
    # => set에 각 라운드별 R, S, P를 넣고 set의 길이가 1, 3이면 다음라운드로
    # 길이가2면 승부가 난걸로

    # 2. 로봇들 승패 구분



