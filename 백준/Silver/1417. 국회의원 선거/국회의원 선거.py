import sys

n = int(input())
if n == 1:
    print(0)
else:
    cand = [int(input()) for _ in range(n)]
    # print(cand)

    lst = cand[1:]
    lst.sort(reverse=True)

    me = cand[0]
    cnt = 0

    while True:
        if me > lst[0]:
            break

        else:
            lst[0] -= 1
            me += 1
            cnt += 1
            lst.sort(reverse=True)

    print(cnt)