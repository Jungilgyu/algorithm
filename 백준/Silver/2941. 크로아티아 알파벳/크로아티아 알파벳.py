import sys
input = sys.stdin.readline

word = input().strip()
n = len(word)
idx = 0

c = ("c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z=")

for char in c:
    word = word.replace(char, '*')

print(len(word))