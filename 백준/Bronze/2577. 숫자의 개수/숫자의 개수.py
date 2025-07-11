import sys

a = int(input())
b = int(input())
c = int(input())

res = a*b*c
res = str(res)


cnt = [0] * 10
for i in range(len(res)):
    temp = int(res[i])
    cnt[temp] += 1


for x in cnt:
    print(x)