import sys

p = int(input())

for _ in range(p):
    class_num = list(map(int, input().split()))
    t = class_num[0]
    children = []
    for i in range(20):
        s = class_num[i+1]
        children.append(s)
    res = [children[0]]
    cnt = 0
    for i in range(1, 20):
        res.append(children[i])
        idx = 0
        for j in range(i):
            if children[j] > children[i]:
                new_res = res[:j-1] + [children[i]] + res[j:19]
                res = new_res
                cnt += 1

    print(t, cnt)


