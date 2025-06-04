import sys

n = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))


total = 0
temp = price[0]

for i in range(1, n):
    if temp > price[i]:
        total += temp * road[i-1]
        temp = price[i]
    else:
        total += temp * road[i-1]
print(total)


