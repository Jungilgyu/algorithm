import sys
import math

n = int(input())

def check(num):
    if int(num) <= 1:
        return False
     # 1000 0000
    for j in range(2, int(math.sqrt(int(num))) + 1):
        if int(num) % j == 0:
            return False
    return True

def backtracking(num):
    if not check(num):
        return

    if len(num) == n:
        print(num)
        return

    for i in range(1, 10, 2): # 5
        nxt = num + str(i)
        backtracking(nxt)


for start in range(2, 10): # 5
    if check(str(start)):
        backtracking(str(start))
