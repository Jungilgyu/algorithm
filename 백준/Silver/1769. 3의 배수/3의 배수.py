import sys
start = input()
find = False
cnt = 0
while True:
    if int(start) < 10:
        if int(start) % 3 == 0:
            find = True
        break

    cnt += 1
    temp = 0
    for num in start:
        temp += int(num)

    if temp < 10:
        if temp == 3 or temp == 6 or temp == 9:
            find = True
        break

    else:
        start = str(temp)

if find:
    print(cnt)
    print("YES")
else:
    print(cnt)
    print("NO")















