import sys
import re
#sys.stdin = open('input.txt')

n = int(input())
input = sys.stdin.readline
pattern = re.compile(r'(100+1+|01)+')

for _ in range(n):
    s = input().strip()
    if pattern.fullmatch(s):
        print("YES")
    else:
        print("NO")