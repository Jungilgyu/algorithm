import sys
input = sys.stdin.readline

count = [0] * 10
n = input().strip()
for num in n:
    if num == '9':
        if count[int(num)] -1 == count[6]:
            count[6] += 1
        else:
            count[int(num)] += 1
    elif num == '6':
        if count[int(num)] -1 == count[9]:
            count[9] += 1
        else:
            count[int(num)] += 1
    else:
        count[int(num)] += 1

print(max(count))




