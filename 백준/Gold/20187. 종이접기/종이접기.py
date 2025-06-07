import sys

k = int(input())
orders = list(input().split())
hole = int(input())

paper = [[hole]]
while orders:
    order = orders.pop()
    new_paper = []
    # 오른쪽 ok
    if order == "R":
        for row in paper:
            temp = []
            for num in row:
                if num == 0:
                    temp.append(1)
                elif num == 1:
                    temp.append(0)
                elif num == 2:
                    temp.append(3)
                else:
                    temp.append(2)
            temp.reverse()
            temp.extend(row)
            new_paper.append(temp)
        paper = new_paper

    elif order == "L":
        for row in paper:
            temp = []
            for num in row:
                if num == 0:
                    temp.append(1)
                elif num == 1:
                    temp.append(0)
                elif num == 2:
                    temp.append(3)
                else:
                    temp.append(2)
            temp.reverse()
            new_temp = row + temp

            new_paper.append(new_temp)
        paper = new_paper

    # 아래 ok
    elif order == "D":
        plus = []
        for row in paper:
            temp = []
            for num in row:
                if num == 0:
                    temp.append(2)
                elif num == 1:
                    temp.append(3)
                elif num == 2:
                    temp.append(0)
                else:
                    temp.append(1)
            plus.append(temp)
        plus.reverse()
        paper = plus + paper

    # 위로
    elif order == "U":
        plus = []
        for row in paper:
            temp = []
            for num in row:
                if num == 0:
                    temp.append(2)
                elif num == 1:
                    temp.append(3)
                elif num == 2:
                    temp.append(0)
                else:
                    temp.append(1)
            plus.append(temp)
        plus.reverse()
        paper = paper + plus
    # for x in paper:
    #     print(x)
for x in paper:
    print(' '.join(map(str, x)))
# 0 => R이나 L만나면, 1 / U나 D만나면 2
# 1 => R이나 L만나면 0 /U나 D만나면 3
# 2 => R이나 L만나면 3 / U나 D 만나면 0
# 3 => R이나 L만나면 2/ U나 D만나면 1

# p = [[1, 2, 3], [4, 5, 6]]