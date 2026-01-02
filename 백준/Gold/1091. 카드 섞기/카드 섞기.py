import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))
s = list(map(int, input().split()))

def check(cards):
    for i in range(n):
        c = cards[i]
        # 0 1 2
        if p[c] != i % 3:
            return False
    return True

def suffle(cards):
    new = [-1] * n
    for i in range(n):
        new[s[i]] = cards[i]
    return new

start = [i for i in range(n)]
cards = [i for i in range(n)] # 카드
cnt = 0

while True:
    if check(cards):
        print(cnt)
        break

    cards = suffle(cards)
    cnt += 1

    if cards == start:
        print(-1)
        break

    # 셔플

