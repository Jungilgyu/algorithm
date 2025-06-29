import sys

scenario = 1
while True:
    n = int(input())
    if n == 0:
        break

    name = []
    earring = [1] * n # 귀걸이를 가지고 시작

    for _ in range(n):
        s = input()
        name.append(s)

    for _ in range(2*n-1):
        s_num, mark = map(str, input().split())
        target = int(s_num)
        earring[target-1] = 1 - earring[target-1]

    # print(earring)
    for i in range(n):
        if earring[i] == 0:
            print(f"{scenario} {name[i]}")
            break

    scenario += 1







