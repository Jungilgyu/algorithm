import sys

n, t = input().rstrip().split()
n = int(n)
# print(type(n))

# Y 윷놀이, F같은그림찾기, O원카드
lst = set()
for _ in range(n):
    name = input()
    lst.add(name)
# print(lst)
ans = 0
if t == "Y": # 2명
    ans = len(lst)

elif t == "F": #3명
    temp = []
    for p in lst:
        if len(temp) < 2:
            temp.append(p)
            if len(temp) == 2:
                temp = []
                ans += 1

else: # 원카드 4명
    temp = []
    for p in lst:
        if len(temp) < 3:
            temp.append(p)
            if len(temp) == 3:
                temp = []
                ans += 1
print(ans)