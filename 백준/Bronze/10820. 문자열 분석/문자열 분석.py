import sys

for line in sys.stdin:
    line = line.rstrip('\n')
    s = b = num = blank = 0

    for x in line:
        if x.islower():
            s += 1
        elif x.isupper():
            b += 1
        elif x.isdigit():
            num += 1
        elif x.isspace():
            blank += 1

    print(s, b, num, blank)
