import sys

n = list(input())
cnt_0 = 0
for num in n:
    if num == '0':
        cnt_0 += 1

if cnt_0 == 0:
    print(-1)
    exit()
else:
    lst = 0
    for num in n:
        lst += int(num)

    if lst % 3 != 0:
        print(-1)
    else:
        n.sort(reverse=True)
        ans = ''.join(map(str, n))
        print(int(ans))

