import sys
input = sys.stdin.readline

s = input().strip()
length = 0
ss = ""
for char in s:
    ss += char
    length += 1
    if length == 10:
        print(ss)
        ss = ""
        length = 0

print(ss)




