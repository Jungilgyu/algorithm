import sys
input = sys.stdin.readline


word = input()

res = ""
for char in word:
    if char.isupper():
        res += char.lower()
    elif char.islower():
        res += char.upper()

print(res)