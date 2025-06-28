import sys


n = int(input())


line = 1
while n > line:
    n -= line
    line += 1

if line % 2 == 0:
    child = n
    parent = line - n + 1

else:
    child = line - n + 1
    parent = n

print(f"{child}/{parent}")
