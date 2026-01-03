import sys
input = sys.stdin.readline

def check(num):
    c = []
    for i in range(4):
        c.append(int(num[i:] + num[:i]))
    return int(num) == min(c)

cards = list(input().split())
nums = []
for i in range(4):
    nums.append(int(''.join(cards[i:] + cards[:i])))

my_num = min(nums)

rank = 0
temp = 1111
while True:
    if '0' not in str(temp) and check(str(temp)):
        rank += 1
        if temp == my_num:
            print(rank)
            break
    temp += 1











