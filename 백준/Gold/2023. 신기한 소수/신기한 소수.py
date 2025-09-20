import sys
import math

n = int(input())

def check(ss):
    num = int(ss)
    if num < 2:
        return False
    if num in (2, 3):
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False

    limit = int(math.sqrt(num)) + 1
    for i in range(5, limit, 6):
        if num % i == 0 or num % (i + 2) == 0:
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
